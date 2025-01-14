import os

import numpy as np
import param

import larvaworld
from larvaworld.lib import reg, aux, util

Path = aux.AttrDict({k : f'{reg.CONF_DIR}/{k}.txt' for k in reg.CONFTYPES})





def build_ConfTypeSubkeys():
    d0 = {k: {} for k in reg.CONFTYPES}
    d1 = {
        'Batch': {'exp': 'Exp'},
        'Ga': {'env_params': 'Env'},
        'Exp': {'env_params': 'Env',
                'trials': 'Trial',
                'larva_groups': 'Model',
                }
    }
    d0.update(d1)
    return aux.AttrDict(d0)

CONFTYPE_SUBKEYS = build_ConfTypeSubkeys()


def build_GroupTypeSubkeys():
    d0 = {k: {} for k in reg.GROUPTYPES}
    d1 = {
        'LarvaGroup': {'Model'},
        # 'Ga': {'env_params': 'Env'},
        # 'Exp': {'env_params': 'Env',
        #         'trials': 'Trial',
        #         'larva_groups': 'Model',
        #         }
    }
    d0.update(d1)
    return aux.AttrDict(d0)

GROUPTYPE_SUBKEYS = build_GroupTypeSubkeys()


CONFTREE = aux.AttrDict({k : aux.load_dict(Path[k]) for k in reg.CONFTYPES})
#
# def build_conf_tree_expanded():
#     c0 = aux.AttrDict({k : aux.load_dict(Path[k]) for k in reg.CONFTYPES})
#     sk = CONFTYPE_SUBKEYS
#     for confType0 in c0.keys():
#         if confType0 in sk.keys():
#             pairs = sk[confType0]
#             for id, conf in c0[confType0].items():
#                 for subID, confType in pairs.items():
#
#
#                     if subID in conf.keys():
#                         if isinstance(conf[subID], str) and conf[subID] in c0[confType].keys():
#                             conf[subID]=c0[confType][conf[subID]]
#                         elif (subID, confType) == ('larva_groups', 'Model'):
#                             for gID, gConf in conf[subID].items():
#                                 mID=gConf.model
#                                 if mID in c0['Model'].keys():
#                                     gConf.model=c0['Model'][mID]
#                                 else:
#                                     # print(f'{mID} not found')
#                                     pass
#                                     # raise
#     return c0
#
# CONFTREE_EXPANDED = build_conf_tree_expanded()


class BaseType:
    def __init__(self, k):
        self.k = k
        if k in reg.par.PI.keys():
            self.dict0 = reg.par.PI[k]
            self.mdict = util.init2mdict(self.dict0)
            self.ks = util.get_ks(self.mdict)
        else:
            self.dict0 = None
            self.mdict = None
            self.ks = None


    def gConf_kws(self, dic):
        kws0 = {}
        for k, kws in dic.items():
            m0 = self.mdict[k]
            kws0[k] = self.gConf(m0, **kws)
        return aux.AttrDict(kws0)

    def gConf(self, m0=None, kwdic=None, **kwargs):
        if m0 is None:
            if self.mdict is None:
                return None
            else:
                m0 = self.mdict
        if kwdic is not None:
            kws0 = self.gConf_kws(kwdic)
            kwargs.update(kws0)

        return aux.AttrDict(util.gConf(m0, **kwargs))

    def entry(self, id, **kwargs):
        return aux.AttrDict({id: self.gConf(**kwargs)})



def lgs(mIDs, ids=None, cs=None,**kwargs):

    if ids is None:
        ids = mIDs
    N = len(mIDs)
    if cs is None :
        cs = aux.N_colors(N)
    return aux.AttrDict(aux.merge_dicts([lg(id, c=c, mID=mID, **kwargs) for mID, c, id in zip(mIDs, cs, ids)]))


def lg(id=None, c='black', N=1, mode='uniform', sh='circle', loc=(0.0, 0.0), ors=(0.0, 360.0),
       s=(0.0, 0.0), mID='explorer',age=0.0, epochs={},  o=None,sample = None, expand=False, **kwargs):

    if mID is not None :
        m = mID if not expand else reg.conf.Model.getID(mID)
        if id is None:
            id=mID
    else :
        m=None
    if id is None:
        id='LarvaGroup'

    if type(s) == float:
        s = (s, s)
    kws = {'kwdic': {
        'distribution': {'N': N, 'scale': s, 'orientation_range': ors, 'loc': loc, 'shape': sh, 'mode': mode},
        'life_history': {'age': age,'epochs': epochs}
    },
           'default_color': c, 'model': m,'sample':sample,  **kwargs}
    if o is not None:
        kws['odor'] = o

    return stored.group.LarvaGroup.entry(id=id, **kws)







def next_idx(id, conftype='Exp'):
    f = f'{reg.CONF_DIR}/SimIdx.txt'
    if not os.path.isfile(f):
        d = aux.AttrDict({k: {} for k in ['Exp', 'Batch', 'Essay', 'Eval', 'Ga']})
    else:
        d = aux.load_dict(f)

    if not conftype in d.keys():
        d[conftype] = {}
    if not id in d[conftype].keys():
        d[conftype][id] = 0
    d[conftype][id] += 1
    aux.save_dict(d, f)
    return d[conftype][id]



class StoredConfRegistry :
    def __init__(self):
        self.group=aux.AttrDict({k: BaseType(k=k) for k in reg.GROUPTYPES})
        self.conf=aux.AttrDict({k: BaseType(k=k) for k in reg.CONFTYPES})



def imitation_exp(refID, model='explorer', **kwargs):
    c = reg.getRef(refID)

    kws = {
        'id': 'ImitationGroup',
        'expand': True,
        'sample': refID,
        'model': model,
        'default_color': 'blue',
        'distribution': {'N': c.N},
        'imitation': True,

    }


    exp_conf = reg.get_null('Exp', sim_params=reg.get_null('sim_params', dt=c.dt, duration=c.duration),
                            env_params=c.env_params, larva_groups=reg.full_lg(**kws),experiment='imitation',
                            trials={}, enrichment=reg.gen.EnrichConf().nestedConf)
    exp_conf.update(**kwargs)
    return exp_conf


stored=StoredConfRegistry()

