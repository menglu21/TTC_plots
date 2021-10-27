import ROOT
import time
import os
import math
from math import sqrt
import plot_TTCregion

TTC_header_path = os.path.join("TTC.h")
ROOT.gInterpreter.Declare('#include "{}"'.format(TTC_header_path))


# the EnableImplicitMT option should only use in cluster, at lxplus, it will make the code slower(my experience)
#ROOT.ROOT.EnableImplicitMT()

def overunder_flowbin(h1):
  h1.SetBinContent(1,h1.GetBinContent(0)+h1.GetBinContent(1))
  h1.SetBinError(1,sqrt(h1.GetBinError(0)*h1.GetBinError(0)+h1.GetBinError(1)*h1.GetBinError(1)))
  h1.SetBinContent(h1.GetNbinsX(),h1.GetBinContent(h1.GetNbinsX())+h1.GetBinContent(h1.GetNbinsX()+1))
  h1.SetBinError(h1.GetNbinsX(),sqrt(h1.GetBinError(h1.GetNbinsX())*h1.GetBinError(h1.GetNbinsX())+h1.GetBinError(h1.GetNbinsX()+1)*h1.GetBinError(h1.GetNbinsX()+1)))
  return h1

def get_mcEventnumber(filename):
  print 'opening file ', filename
  nevent_temp=0
  for i in range(0,len(filename)):
    ftemp=ROOT.TFile.Open(filename[i])
    htemp=ftemp.Get('nEventsGenWeighted')
    nevent_temp=nevent_temp+htemp.GetBinContent(1)
  return nevent_temp

def all_trigger(df):
  all_trigger = df.Filter("HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8 || HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ || HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ || HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ || HLT_IsoMu27 || HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL || HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ || HLT_passEle32WPTight || HLT_Ele35_WPTight_Gsf")
  return all_trigger

def for_diele_trigger(df):
  ditri_ele_trigger = df.Filter("HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL || HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ")
  return ditri_ele_trigger

def for_singleele_trigger_eechannel(df):
  sin_ele_trigger = df.Filter("!(HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL) && !(HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ) && (HLT_passEle32WPTight || HLT_Ele35_WPTight_Gsf)")
  return sin_ele_trigger

def for_singleele_trigger_emuchannel(df):
  sin_ele_trigger = df.Filter("!(HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ) && !(HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ) && !(HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ) && (HLT_passEle32WPTight || HLT_Ele35_WPTight_Gsf)")
  return sin_ele_trigger

def for_dimuon_trigger(df):
  ditri_mu_trigger = df.Filter("(HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8)")
  return ditri_mu_trigger

def for_singlemuon_trigger_mumuchannel(df):
  single_mu_trigger = df.Filter("!(HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8) && HLT_IsoMu27")
  return single_mu_trigger

def for_singlemuon_trigger_emuchannel(df):
  single_mu_trigger = df.Filter("!(HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ || HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ || HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ) && HLT_IsoMu27")
  return single_mu_trigger

def for_cross_trigger(df):
  x_trigger = df.Filter("(HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ || HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ || HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ)")
  return x_trigger

path='/eos/user/m/melu/TTC_Nanov8_new/'
path_fake='/eos/user/m/melu/TTC_Nanov8_new/FakeLep/'

doubleEle_names = ROOT.std.vector('string')()
for f in ["DoubleEGB.root","DoubleEGC.root","DoubleEGD.root","DoubleEGE.root","DoubleEGF.root"]:
  doubleEle_names.push_back(path+f)

singleEle_names = ROOT.std.vector('string')()
for f in ["SingleEGB.root","SingleEGC.root","SingleEGD.root","SingleEGE.root","SingleEGF.root"]:
  singleEle_names.push_back(path+f)

FakeLep_doubleEle_names = ROOT.std.vector('string')()
for f in ["DoubleEGB.root","DoubleEGC.root","DoubleEGD.root","DoubleEGE.root","DoubleEGF.root"]:
  FakeLep_doubleEle_names.push_back(path_fake+f)

FakeLep_singleEle_names = ROOT.std.vector('string')()
for f in ["SingleEGB.root","SingleEGC.root","SingleEGD.root","SingleEGE.root","SingleEGF.root"]:
  FakeLep_singleEle_names.push_back(path_fake+f)

DY_list = ROOT.std.vector('string')()
for f in ['DY.root']:
  DY_list.push_back(path+f)

Fake_DY_list = ROOT.std.vector('string')()
for f in ['DY.root']:
  Fake_DY_list.push_back(path_fake+f)

WW_list = ROOT.std.vector('string')()
for f in ['WW.root']:
  WW_list.push_back(path+f)

Fake_WW_list = ROOT.std.vector('string')()
for f in ['WW.root']:
  Fake_WW_list.push_back(path_fake+f)

WZ_list = ROOT.std.vector('string')()
for f in ['WZ.root']:
  WZ_list.push_back(path+f)

Fake_WZ_list = ROOT.std.vector('string')()
for f in ['WZ.root']:
  Fake_WZ_list.push_back(path_fake+f)

ZZ_list = ROOT.std.vector('string')()
for f in ['ZZ.root']:
  ZZ_list.push_back(path+f)

Fake_ZZ_list = ROOT.std.vector('string')()
for f in ['ZZ.root']:
  Fake_ZZ_list.push_back(path_fake+f)

WWW_list = ROOT.std.vector('string')()
for f in ['WWW.root']:
  WWW_list.push_back(path+f)

Fake_WWW_list = ROOT.std.vector('string')()
for f in ['WWW.root']:
  Fake_WWW_list.push_back(path_fake+f)

WWZ_list = ROOT.std.vector('string')()
for f in ['WWZ.root']:
  WWZ_list.push_back(path+f)

Fake_WWZ_list = ROOT.std.vector('string')()
for f in ['WWZ.root']:
  Fake_WWZ_list.push_back(path_fake+f)

WZZ_list = ROOT.std.vector('string')()
for f in ['WZZ.root']:
  WZZ_list.push_back(path+f)

Fake_WZZ_list = ROOT.std.vector('string')()
for f in ['WZZ.root']:
  Fake_WZZ_list.push_back(path_fake+f)

ZZZ_list = ROOT.std.vector('string')()
for f in ['ZZZ.root']:
  ZZZ_list.push_back(path+f)

Fake_ZZZ_list = ROOT.std.vector('string')()
for f in ['ZZZ.root']:
  Fake_ZZZ_list.push_back(path_fake+f)

tW_list = ROOT.std.vector('string')()
for f in ['tW.root']:
  tW_list.push_back(path+f)

Fake_tW_list = ROOT.std.vector('string')()
for f in ['tW.root']:
  Fake_tW_list.push_back(path_fake+f)

tbarW_list = ROOT.std.vector('string')()
for f in ['tbarW.root']:
  tbarW_list.push_back(path+f)

Fake_tbarW_list = ROOT.std.vector('string')()
for f in ['tbarW.root']:
  Fake_tbarW_list.push_back(path_fake+f)

ttWtoLNu_list = ROOT.std.vector('string')()
for f in ['ttWtoLNu.root']:
  ttWtoLNu_list.push_back(path+f)

Fake_ttWtoLNu_list = ROOT.std.vector('string')()
for f in ['ttWtoLNu.root']:
  Fake_ttWtoLNu_list.push_back(path_fake+f)

ttWtoQQ_list = ROOT.std.vector('string')()
for f in ['ttWtoQQ.root']:
  ttWtoQQ_list.push_back(path+f)

Fake_ttWtoQQ_list = ROOT.std.vector('string')()
for f in ['ttWtoQQ.root']:
  Fake_ttWtoQQ_list.push_back(path_fake+f)

ttZ_list = ROOT.std.vector('string')()
for f in ['ttZ.root']:
  ttZ_list.push_back(path+f)

Fake_ttZ_list = ROOT.std.vector('string')()
for f in ['ttZ.root']:
  Fake_ttZ_list.push_back(path_fake+f)

ttZtoQQ_list = ROOT.std.vector('string')()
for f in ['ttZtoQQ.root']:
  ttZtoQQ_list.push_back(path+f)

Fake_ttZtoQQ_list = ROOT.std.vector('string')()
for f in ['ttZtoQQ.root']:
  Fake_ttZtoQQ_list.push_back(path_fake+f)

ttH_list = ROOT.std.vector('string')()
for f in ['ttH.root']:
  ttH_list.push_back(path+f)

Fake_ttH_list = ROOT.std.vector('string')()
for f in ['ttH.root']:
  Fake_ttH_list.push_back(path_fake+f)

ttWW_list = ROOT.std.vector('string')()
for f in ['ttWW.root']:
  ttWW_list.push_back(path+f)

Fake_ttWW_list = ROOT.std.vector('string')()
for f in ['ttWW.root']:
  Fake_ttWW_list.push_back(path_fake+f)

ttWZ_list = ROOT.std.vector('string')()
for f in ['ttWZ.root']:
  ttWZ_list.push_back(path+f)

Fake_ttWZ_list = ROOT.std.vector('string')()
for f in ['ttWZ.root']:
  Fake_ttWZ_list.push_back(path_fake+f)

ttZZ_list = ROOT.std.vector('string')()
for f in ['ttZZ.root']:
  ttZZ_list.push_back(path+f)

Fake_ttZZ_list = ROOT.std.vector('string')()
for f in ['ttZZ.root']:
  Fake_ttZZ_list.push_back(path_fake+f)

tzq_list = ROOT.std.vector('string')()
for f in ['tzq.root']:
  tzq_list.push_back(path+f)

Fake_tzq_list = ROOT.std.vector('string')()
for f in ['tzq.root']:
  Fake_tzq_list.push_back(path_fake+f)

TTTo2L_list = ROOT.std.vector('string')()
for f in ['TTTo2L.root']:
  TTTo2L_list.push_back(path+f)

Fake_TTTo2L_list = ROOT.std.vector('string')()
for f in ['TTTo2L.root']:
  Fake_TTTo2L_list.push_back(path_fake+f)

#histograms name
hists_name = ['ttc_l1_pt','ttc_l1_eta','ttc_l1_phi','ttc_l2_pt','ttc_l2_eta','ttc_l2_phi','ttc_mll','ttc_drll','ttc_dphill','ttc_met','ttc_met_phi','j1_pt','j1_eta','j1_phi','j1_mass','j2_pt','j2_eta','j2_phi','j2_mass','j3_pt','j3_eta','j3_phi','j3_mass','n_tight_jet','ttc_mllj1','ttc_mllj2','ttc_mllj3','ttc_dr_l1j1','ttc_dr_l1j2','ttc_dr_l1j3','ttc_dr_l2j1','ttc_dr_l2j2','ttc_dr_l2j3']

#histograms bins
histos_bins = {
hists_name[0]:20,
hists_name[1]:20,
hists_name[2]:20,
hists_name[3]:20,
hists_name[4]:20,
hists_name[5]:20,
hists_name[6]:50,
hists_name[7]:20,
hists_name[8]:20,
hists_name[9]:20,
hists_name[10]:20,
hists_name[11]:30,
hists_name[12]:20,
hists_name[13]:20,
hists_name[14]:10,
hists_name[15]:20,
hists_name[16]:20,
hists_name[17]:20,
hists_name[18]:10,
hists_name[19]:20,
hists_name[20]:20,
hists_name[21]:20,
hists_name[22]:10,
hists_name[23]:10,
hists_name[24]:20,
hists_name[25]:20,
hists_name[26]:20,
hists_name[27]:20,
hists_name[28]:20,
hists_name[29]:20,
hists_name[30]:20,
hists_name[31]:20,
hists_name[32]:20,
}

#low edge
histos_bins_low = {
hists_name[0]:0,
hists_name[1]:-3,
hists_name[2]:-4,
hists_name[3]:0,
hists_name[4]:-3,
hists_name[5]:-4,
hists_name[6]:0,
hists_name[7]:0,
hists_name[8]:-4,
hists_name[9]:0,
hists_name[10]:-4,
hists_name[11]:0,
hists_name[12]:-3,
hists_name[13]:-4,
hists_name[14]:0,
hists_name[15]:0,
hists_name[16]:-3,
hists_name[17]:-4,
hists_name[18]:0,
hists_name[19]:0,
hists_name[20]:-3,
hists_name[21]:-4,
hists_name[22]:0,
hists_name[23]:0,
hists_name[24]:0,
hists_name[25]:0,
hists_name[26]:0,
hists_name[27]:0,
hists_name[28]:0,
hists_name[29]:0,
hists_name[30]:0,
hists_name[31]:0,
hists_name[32]:0,
}

#high edge
histos_bins_high = {
hists_name[0]:200,
hists_name[1]:3,
hists_name[2]:4,
hists_name[3]:100,
hists_name[4]:3,
hists_name[5]:4,
hists_name[6]:400,
hists_name[7]:5,
hists_name[8]:4,
hists_name[9]:300,
hists_name[10]:4,
hists_name[11]:400,
hists_name[12]:3,
hists_name[13]:4,
hists_name[14]:50,
hists_name[15]:200,
hists_name[16]:3,
hists_name[17]:4,
hists_name[18]:50,
hists_name[19]:200,
hists_name[20]:3,
hists_name[21]:4,
hists_name[22]:50,
hists_name[23]:10,
hists_name[24]:800,
hists_name[25]:500,
hists_name[26]:500,
hists_name[27]:5,
hists_name[28]:5,
hists_name[29]:5,
hists_name[30]:5,
hists_name[31]:5,
hists_name[32]:5,
}

def TTC_Analysis():

  histos = []

  lumi = 41480.

  DY_xs = 6077.22
  DY_ev = get_mcEventnumber(DY_list)
  Fake_DY_ev = get_mcEventnumber(Fake_DY_list)

  WW_xs = 118.7
  WW_ev = get_mcEventnumber(WW_list)
  Fake_WW_ev = get_mcEventnumber(Fake_WW_list)

  WZ_xs = 65.5443
  WZ_ev = get_mcEventnumber(WZ_list)
  Fake_WZ_ev = get_mcEventnumber(Fake_WZ_list)

  ZZ_xs = 15.8274
  ZZ_ev = get_mcEventnumber(ZZ_list)
  Fake_ZZ_ev = get_mcEventnumber(Fake_ZZ_list)

  WWW_xs = 0.2086
  WWW_ev = get_mcEventnumber(WWW_list)
  Fake_WWW_ev = get_mcEventnumber(Fake_WWW_list)

  WWZ_xs = 0.1707
  WWZ_ev = get_mcEventnumber(WWZ_list)
  Fake_WWZ_ev = get_mcEventnumber(Fake_WWZ_list)

  WZZ_xs = 0.05709
  WZZ_ev = get_mcEventnumber(WZZ_list)
  Fake_WZZ_ev = get_mcEventnumber(Fake_WZZ_list)

  ZZZ_xs = 0.01476
  ZZZ_ev = get_mcEventnumber(ZZZ_list)
  Fake_ZZZ_ev = get_mcEventnumber(Fake_ZZZ_list)

  TTTo2L_xs = 88.3419
  TTTo2L_ev = get_mcEventnumber(TTTo2L_list)
  Fake_TTTo2L_ev = get_mcEventnumber(Fake_TTTo2L_list)

  TTH_xs = 0.5269
  TTH_ev = get_mcEventnumber(ttH_list)
  Fake_TTH_ev = get_mcEventnumber(Fake_ttH_list)

  TTWtoLNu_xs = 0.1792
  TTWtoLNu_ev = get_mcEventnumber(ttWtoLNu_list)
  Fake_TTWtoLNu_ev = get_mcEventnumber(Fake_ttWtoLNu_list)

  TTWtoQQ_xs = 0.3708
  TTWtoQQ_ev = get_mcEventnumber(ttWtoQQ_list)
  Fake_TTWtoQQ_ev = get_mcEventnumber(Fake_ttWtoQQ_list)

  TTZ_xs = 0.2589
  TTZ_ev = get_mcEventnumber(ttZ_list)
  Fake_TTZ_ev = get_mcEventnumber(Fake_ttZ_list)

  TTZtoQQ_xs = 0.6012
  TTZtoQQ_ev = get_mcEventnumber(ttZtoQQ_list)
  Fake_TTZtoQQ_ev = get_mcEventnumber(Fake_ttZtoQQ_list)

  TTWW_xs = 0.007003
  TTWW_ev = get_mcEventnumber(ttWW_list)
  Fake_TTWW_ev = get_mcEventnumber(Fake_ttWW_list)

  TTWZ_xs = 0.002453
  TTWZ_ev = get_mcEventnumber(ttWZ_list)
  Fake_TTWZ_ev = get_mcEventnumber(Fake_ttWZ_list)

  TTZZ_xs = 0.001386
  TTZZ_ev = get_mcEventnumber(ttZZ_list)
  Fake_TTZZ_ev = get_mcEventnumber(Fake_ttZZ_list)

  tZq_xs = 0.07561
  tZq_ev = get_mcEventnumber(tzq_list)
  Fake_tZq_ev = get_mcEventnumber(Fake_tzq_list)

  tW_xs = 35.85
  tW_ev = get_mcEventnumber(tW_list)
  Fake_tW_ev = get_mcEventnumber(Fake_tW_list)

  tbarW_xs = 35.85
  tbarW_ev = get_mcEventnumber(tbarW_list)
  Fake_tbarW_ev = get_mcEventnumber(Fake_tbarW_list)

  # define the filters here, 1:2mu, 2:1e1m, 3:2ele
  filters="ttc_jets && ttc_region==3 && ttc_l1_pt>30 && ttc_met>30 && ttc_mll>20 && ttc_drll>0.3 && Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_eeBadScFilter && Flag_ecalBadCalibFilter && nGenDressedLepton>1"
  filters_data="ttc_jets && ttc_region==3 && ttc_l1_pt>30 && ttc_met>30 && ttc_mll>20 && ttc_drll>0.3 && Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_eeBadScFilter && Flag_ecalBadCalibFilter"
  filters_fake_mc="ttc_jets && ttc_region==3 && ttc_l1_pt>30 && ttc_met>30 && ttc_mll>20 && ttc_drll>0.3 && Flag_goodVertices && Flag_globalSuperTightHalo2016Filter && Flag_HBHENoiseFilter && Flag_HBHENoiseIsoFilter && Flag_EcalDeadCellTriggerPrimitiveFilter && Flag_BadPFMuonFilter && Flag_eeBadScFilter && Flag_ecalBadCalibFilter && lhe_nlepton>1"

  df_DY_tree = ROOT.RDataFrame("Events",DY_list)
  df_DY_tree = df_DY_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_DY_tree = df_DY_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_DY = df_DY_tree.Filter(filters)
  df_DY_trigger = all_trigger(df_DY)
  df_DY_histos=[]
  for i in hists_name:
    df_DY_histo = df_DY_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_DY_histos.append(df_DY_histo)

  df_Fake_DY_tree = ROOT.RDataFrame("Events",Fake_DY_list)
  df_Fake_DY_tree = df_Fake_DY_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_DY_tree = df_Fake_DY_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_DY_tree = df_Fake_DY_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_DY = df_Fake_DY_tree.Filter(filters_fake_mc)
  df_Fake_DY_trigger = all_trigger(df_Fake_DY)
  df_Fake_DY_histos=[]
  for i in hists_name:
    df_Fake_DY_histo = df_Fake_DY_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_DY_histos.append(df_Fake_DY_histo)

  df_WW_tree = ROOT.RDataFrame("Events",WW_list)
  df_WW_tree = df_WW_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_WW_tree = df_WW_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_WW = df_WW_tree.Filter(filters)
  df_WW_trigger = all_trigger(df_WW)
  df_WW_histos=[]
  for i in hists_name:
    df_WW_histo = df_WW_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_WW_histos.append(df_WW_histo)

  df_Fake_WW_tree = ROOT.RDataFrame("Events",Fake_WW_list)
  df_Fake_WW_tree = df_Fake_WW_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_WW_tree = df_Fake_WW_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_WW_tree = df_Fake_WW_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_WW = df_Fake_WW_tree.Filter(filters_fake_mc)
  df_Fake_WW_trigger = all_trigger(df_Fake_WW)
  df_Fake_WW_histos=[]
  for i in hists_name:
    df_Fake_WW_histo = df_Fake_WW_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_WW_histos.append(df_Fake_WW_histo)

  df_WZ_tree = ROOT.RDataFrame("Events",WZ_list)
  df_WZ_tree = df_WZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_WZ_tree = df_WZ_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_WZ = df_WZ_tree.Filter(filters)
  df_WZ_trigger = all_trigger(df_WZ)
  df_WZ_histos=[]
  for i in hists_name:
    df_WZ_histo = df_WZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_WZ_histos.append(df_WZ_histo)

  df_Fake_WZ_tree = ROOT.RDataFrame("Events",Fake_WZ_list)
  df_Fake_WZ_tree = df_Fake_WZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_WZ_tree = df_Fake_WZ_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_WZ_tree = df_Fake_WZ_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_WZ = df_Fake_WZ_tree.Filter(filters_fake_mc)
  df_Fake_WZ_trigger = all_trigger(df_Fake_WZ)
  df_Fake_WZ_histos=[]
  for i in hists_name:
    df_Fake_WZ_histo = df_Fake_WZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_WZ_histos.append(df_Fake_WZ_histo)

  df_ZZ_tree = ROOT.RDataFrame("Events",ZZ_list)
  df_ZZ_tree = df_ZZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_ZZ_tree = df_ZZ_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_ZZ = df_ZZ_tree.Filter(filters)
  df_ZZ_trigger = all_trigger(df_ZZ)
  df_ZZ_histos=[]
  for i in hists_name:
    df_ZZ_histo = df_ZZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_ZZ_histos.append(df_ZZ_histo)

  df_Fake_ZZ_tree = ROOT.RDataFrame("Events",Fake_ZZ_list)
  df_Fake_ZZ_tree = df_Fake_ZZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_ZZ_tree = df_Fake_ZZ_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_ZZ_tree = df_Fake_ZZ_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_ZZ = df_Fake_ZZ_tree.Filter(filters_fake_mc)
  df_Fake_ZZ_trigger = all_trigger(df_Fake_ZZ)
  df_Fake_ZZ_histos=[]
  for i in hists_name:
    df_Fake_ZZ_histo = df_Fake_ZZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_ZZ_histos.append(df_Fake_ZZ_histo)

  df_WWW_tree = ROOT.RDataFrame("Events",WWW_list)
  df_WWW_tree = df_WWW_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_WWW_tree = df_WWW_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_WWW = df_WWW_tree.Filter(filters)
  df_WWW_trigger = all_trigger(df_WWW)
  df_WWW_histos=[]
  for i in hists_name:
    df_WWW_histo = df_WWW_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_WWW_histos.append(df_WWW_histo)

  df_Fake_WWW_tree = ROOT.RDataFrame("Events",Fake_WWW_list)
  df_Fake_WWW_tree = df_Fake_WWW_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_WWW_tree = df_Fake_WWW_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_WWW_tree = df_Fake_WWW_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_WWW = df_Fake_WWW_tree.Filter(filters_fake_mc)
  df_Fake_WWW_trigger = all_trigger(df_Fake_WWW)
  df_Fake_WWW_histos=[]
  for i in hists_name:
    df_Fake_WWW_histo = df_Fake_WWW_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_WWW_histos.append(df_Fake_WWW_histo)

  df_WWZ_tree = ROOT.RDataFrame("Events",WWZ_list)
  df_WWZ_tree = df_WWZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_WWZ_tree = df_WWZ_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_WWZ = df_WWZ_tree.Filter(filters)
  df_WWZ_trigger = all_trigger(df_WWZ)
  df_WWZ_histos=[]
  for i in hists_name:
    df_WWZ_histo = df_WWZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_WWZ_histos.append(df_WWZ_histo)

  df_Fake_WWZ_tree = ROOT.RDataFrame("Events",Fake_WWZ_list)
  df_Fake_WWZ_tree = df_Fake_WWZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_WWZ_tree = df_Fake_WWZ_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_WWZ_tree = df_Fake_WWZ_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_WWZ = df_Fake_WWZ_tree.Filter(filters_fake_mc)
  df_Fake_WWZ_trigger = all_trigger(df_Fake_WWZ)
  df_Fake_WWZ_histos=[]
  for i in hists_name:
    df_Fake_WWZ_histo = df_Fake_WWZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_WWZ_histos.append(df_Fake_WWZ_histo)

  df_WZZ_tree = ROOT.RDataFrame("Events",WZZ_list)
  df_WZZ_tree = df_WZZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_WZZ_tree = df_WZZ_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_WZZ = df_WZZ_tree.Filter(filters)
  df_WZZ_trigger = all_trigger(df_WZZ)
  df_WZZ_histos=[]
  for i in hists_name:
    df_WZZ_histo = df_WZZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_WZZ_histos.append(df_WZZ_histo)

  df_Fake_WZZ_tree = ROOT.RDataFrame("Events",Fake_WZZ_list)
  df_Fake_WZZ_tree = df_Fake_WZZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_WZZ_tree = df_Fake_WZZ_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_WZZ_tree = df_Fake_WZZ_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_WZZ = df_Fake_WZZ_tree.Filter(filters_fake_mc)
  df_Fake_WZZ_trigger = all_trigger(df_Fake_WZZ)
  df_Fake_WZZ_histos=[]
  for i in hists_name:
    df_Fake_WZZ_histo = df_Fake_WZZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_WZZ_histos.append(df_Fake_WZZ_histo)

  df_ZZZ_tree = ROOT.RDataFrame("Events",ZZZ_list)
  df_ZZZ_tree = df_ZZZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_ZZZ_tree = df_ZZZ_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_ZZZ = df_ZZZ_tree.Filter(filters)
  df_ZZZ_trigger = all_trigger(df_ZZZ)
  df_ZZZ_histos=[]
  for i in hists_name:
    df_ZZZ_histo = df_ZZZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_ZZZ_histos.append(df_ZZZ_histo)

  df_Fake_ZZZ_tree = ROOT.RDataFrame("Events",Fake_ZZZ_list)
  df_Fake_ZZZ_tree = df_Fake_ZZZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_ZZZ_tree = df_Fake_ZZZ_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_ZZZ_tree = df_Fake_ZZZ_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_ZZZ = df_Fake_ZZZ_tree.Filter(filters_fake_mc)
  df_Fake_ZZZ_trigger = all_trigger(df_Fake_ZZZ)
  df_Fake_ZZZ_histos=[]
  for i in hists_name:
    df_Fake_ZZZ_histo = df_Fake_ZZZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_ZZZ_histos.append(df_Fake_ZZZ_histo)

  df_tW_tree = ROOT.RDataFrame("Events",tW_list)
  df_tW_tree = df_tW_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_tW_tree = df_tW_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_tW = df_tW_tree.Filter(filters)
  df_tW_trigger = all_trigger(df_tW)
  df_tW_histos=[]
  for i in hists_name:
    df_tW_histo = df_tW_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_tW_histos.append(df_tW_histo)

  df_Fake_tW_tree = ROOT.RDataFrame("Events",Fake_tW_list)
  df_Fake_tW_tree = df_Fake_tW_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_tW_tree = df_Fake_tW_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_tW_tree = df_Fake_tW_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_tW = df_Fake_tW_tree.Filter(filters_fake_mc)
  df_Fake_tW_trigger = all_trigger(df_Fake_tW)
  df_Fake_tW_histos=[]
  for i in hists_name:
    df_Fake_tW_histo = df_Fake_tW_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_tW_histos.append(df_Fake_tW_histo)

  df_tbarW_tree = ROOT.RDataFrame("Events",tbarW_list)
  df_tbarW_tree = df_tbarW_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_tbarW_tree = df_tbarW_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_tbarW = df_tbarW_tree.Filter(filters)
  df_tbarW_trigger = all_trigger(df_tbarW)
  df_tbarW_histos=[]
  for i in hists_name:
    df_tbarW_histo = df_tbarW_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_tbarW_histos.append(df_tbarW_histo)

  df_Fake_tbarW_tree = ROOT.RDataFrame("Events",Fake_tbarW_list)
  df_Fake_tbarW_tree = df_Fake_tbarW_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_tbarW_tree = df_Fake_tbarW_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_tbarW_tree = df_Fake_tbarW_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_tbarW = df_Fake_tbarW_tree.Filter(filters_fake_mc)
  df_Fake_tbarW_trigger = all_trigger(df_Fake_tbarW)
  df_Fake_tbarW_histos=[]
  for i in hists_name:
    df_Fake_tbarW_histo = df_Fake_tbarW_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_tbarW_histos.append(df_Fake_tbarW_histo)

  df_ttWtoLNu_tree = ROOT.RDataFrame("Events",ttWtoLNu_list)
  df_ttWtoLNu_tree = df_ttWtoLNu_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_ttWtoLNu_tree = df_ttWtoLNu_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_ttWtoLNu = df_ttWtoLNu_tree.Filter(filters)
  df_ttWtoLNu_trigger = all_trigger(df_ttWtoLNu)
  df_ttWtoLNu_histos=[]
  for i in hists_name:
    df_ttWtoLNu_histo = df_ttWtoLNu_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_ttWtoLNu_histos.append(df_ttWtoLNu_histo)

  df_Fake_ttWtoLNu_tree = ROOT.RDataFrame("Events",Fake_ttWtoLNu_list)
  df_Fake_ttWtoLNu_tree = df_Fake_ttWtoLNu_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_ttWtoLNu_tree = df_Fake_ttWtoLNu_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_ttWtoLNu_tree = df_Fake_ttWtoLNu_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_ttWtoLNu = df_Fake_ttWtoLNu_tree.Filter(filters_fake_mc)
  df_Fake_ttWtoLNu_trigger = all_trigger(df_Fake_ttWtoLNu)
  df_Fake_ttWtoLNu_histos=[]
  for i in hists_name:
    df_Fake_ttWtoLNu_histo = df_Fake_ttWtoLNu_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_ttWtoLNu_histos.append(df_Fake_ttWtoLNu_histo)

  df_ttWtoQQ_tree = ROOT.RDataFrame("Events",ttWtoQQ_list)
  df_ttWtoQQ_tree = df_ttWtoQQ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_ttWtoQQ_tree = df_ttWtoQQ_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_ttWtoQQ = df_ttWtoQQ_tree.Filter(filters)
  df_ttWtoQQ_trigger = all_trigger(df_ttWtoQQ)
  df_ttWtoQQ_histos=[]
  for i in hists_name:
    df_ttWtoQQ_histo = df_ttWtoQQ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_ttWtoQQ_histos.append(df_ttWtoQQ_histo)

  df_Fake_ttWtoQQ_tree = ROOT.RDataFrame("Events",Fake_ttWtoQQ_list)
  df_Fake_ttWtoQQ_tree = df_Fake_ttWtoQQ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_ttWtoQQ_tree = df_Fake_ttWtoQQ_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_ttWtoQQ_tree = df_Fake_ttWtoQQ_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_ttWtoQQ = df_Fake_ttWtoQQ_tree.Filter(filters_fake_mc)
  df_Fake_ttWtoQQ_trigger = all_trigger(df_Fake_ttWtoQQ)
  df_Fake_ttWtoQQ_histos=[]
  for i in hists_name:
    df_Fake_ttWtoQQ_histo = df_Fake_ttWtoQQ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_ttWtoQQ_histos.append(df_Fake_ttWtoQQ_histo)

  df_ttZ_tree = ROOT.RDataFrame("Events",ttZ_list)
  df_ttZ_tree = df_ttZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_ttZ_tree = df_ttZ_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_ttZ = df_ttZ_tree.Filter(filters)
  df_ttZ_trigger = all_trigger(df_ttZ)
  df_ttZ_histos=[]
  for i in hists_name:
    df_ttZ_histo = df_ttZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_ttZ_histos.append(df_ttZ_histo)

  df_Fake_ttZ_tree = ROOT.RDataFrame("Events",Fake_ttZ_list)
  df_Fake_ttZ_tree = df_Fake_ttZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_ttZ_tree = df_Fake_ttZ_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_ttZ_tree = df_Fake_ttZ_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_ttZ = df_Fake_ttZ_tree.Filter(filters_fake_mc)
  df_Fake_ttZ_trigger = all_trigger(df_Fake_ttZ)
  df_Fake_ttZ_histos=[]
  for i in hists_name:
    df_Fake_ttZ_histo = df_Fake_ttZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_ttZ_histos.append(df_Fake_ttZ_histo)

  df_ttZtoQQ_tree = ROOT.RDataFrame("Events",ttZtoQQ_list)
  df_ttZtoQQ_tree = df_ttZtoQQ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_ttZtoQQ_tree = df_ttZtoQQ_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_ttZtoQQ = df_ttZtoQQ_tree.Filter(filters)
  df_ttZtoQQ_trigger = all_trigger(df_ttZtoQQ)
  df_ttZtoQQ_histos=[]
  for i in hists_name:
    df_ttZtoQQ_histo = df_ttZtoQQ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_ttZtoQQ_histos.append(df_ttZtoQQ_histo)

  df_Fake_ttZtoQQ_tree = ROOT.RDataFrame("Events",Fake_ttZtoQQ_list)
  df_Fake_ttZtoQQ_tree = df_Fake_ttZtoQQ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_ttZtoQQ_tree = df_Fake_ttZtoQQ_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_ttZtoQQ_tree = df_Fake_ttZtoQQ_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_ttZtoQQ = df_Fake_ttZtoQQ_tree.Filter(filters_fake_mc)
  df_Fake_ttZtoQQ_trigger = all_trigger(df_Fake_ttZtoQQ)
  df_Fake_ttZtoQQ_histos=[]
  for i in hists_name:
    df_Fake_ttZtoQQ_histo = df_Fake_ttZtoQQ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_ttZtoQQ_histos.append(df_Fake_ttZtoQQ_histo)

  df_ttH_tree = ROOT.RDataFrame("Events",ttH_list)
  df_ttH_tree = df_ttH_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_ttH_tree = df_ttH_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_ttH = df_ttH_tree.Filter(filters)
  df_ttH_trigger = all_trigger(df_ttH)
  df_ttH_histos=[]
  for i in hists_name:
    df_ttH_histo = df_ttH_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_ttH_histos.append(df_ttH_histo)

  df_Fake_ttH_tree = ROOT.RDataFrame("Events",Fake_ttH_list)
  df_Fake_ttH_tree = df_Fake_ttH_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_ttH_tree = df_Fake_ttH_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_ttH_tree = df_Fake_ttH_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_ttH = df_Fake_ttH_tree.Filter(filters_fake_mc)
  df_Fake_ttH_trigger = all_trigger(df_Fake_ttH)
  df_Fake_ttH_histos=[]
  for i in hists_name:
    df_Fake_ttH_histo = df_Fake_ttH_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_ttH_histos.append(df_Fake_ttH_histo)

  df_ttWW_tree = ROOT.RDataFrame("Events",ttWW_list)
  df_ttWW_tree = df_ttWW_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_ttWW_tree = df_ttWW_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_ttWW = df_ttWW_tree.Filter(filters)
  df_ttWW_trigger = all_trigger(df_ttWW)
  df_ttWW_histos=[]
  for i in hists_name:
    df_ttWW_histo = df_ttWW_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_ttWW_histos.append(df_ttWW_histo)

  df_Fake_ttWW_tree = ROOT.RDataFrame("Events",Fake_ttWW_list)
  df_Fake_ttWW_tree = df_Fake_ttWW_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_ttWW_tree = df_Fake_ttWW_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_ttWW_tree = df_Fake_ttWW_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_ttWW = df_Fake_ttWW_tree.Filter(filters_fake_mc)
  df_Fake_ttWW_trigger = all_trigger(df_Fake_ttWW)
  df_Fake_ttWW_histos=[]
  for i in hists_name:
    df_Fake_ttWW_histo = df_Fake_ttWW_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_ttWW_histos.append(df_Fake_ttWW_histo)

  df_ttWZ_tree = ROOT.RDataFrame("Events",ttWZ_list)
  df_ttWZ_tree = df_ttWZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_ttWZ_tree = df_ttWZ_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_ttWZ = df_ttWZ_tree.Filter(filters)
  df_ttWZ_trigger = all_trigger(df_ttWZ)
  df_ttWZ_histos=[]
  for i in hists_name:
    df_ttWZ_histo = df_ttWZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_ttWZ_histos.append(df_ttWZ_histo)

  df_Fake_ttWZ_tree = ROOT.RDataFrame("Events",Fake_ttWZ_list)
  df_Fake_ttWZ_tree = df_Fake_ttWZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_ttWZ_tree = df_Fake_ttWZ_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_ttWZ_tree = df_Fake_ttWZ_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_ttWZ = df_Fake_ttWZ_tree.Filter(filters_fake_mc)
  df_Fake_ttWZ_trigger = all_trigger(df_Fake_ttWZ)
  df_Fake_ttWZ_histos=[]
  for i in hists_name:
    df_Fake_ttWZ_histo = df_Fake_ttWZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_ttWZ_histos.append(df_Fake_ttWZ_histo)

  df_ttZZ_tree = ROOT.RDataFrame("Events",ttZZ_list)
  df_ttZZ_tree = df_ttZZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_ttZZ_tree = df_ttZZ_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_ttZZ = df_ttZZ_tree.Filter(filters)
  df_ttZZ_trigger = all_trigger(df_ttZZ)
  df_ttZZ_histos=[]
  for i in hists_name:
    df_ttZZ_histo = df_ttZZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_ttZZ_histos.append(df_ttZZ_histo)

  df_Fake_ttZZ_tree = ROOT.RDataFrame("Events",Fake_ttZZ_list)
  df_Fake_ttZZ_tree = df_Fake_ttZZ_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_ttZZ_tree = df_Fake_ttZZ_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_ttZZ_tree = df_Fake_ttZZ_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_ttZZ = df_Fake_ttZZ_tree.Filter(filters_fake_mc)
  df_Fake_ttZZ_trigger = all_trigger(df_Fake_ttZZ)
  df_Fake_ttZZ_histos=[]
  for i in hists_name:
    df_Fake_ttZZ_histo = df_Fake_ttZZ_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_ttZZ_histos.append(df_Fake_ttZZ_histo)

  df_tzq_tree = ROOT.RDataFrame("Events",tzq_list)
  df_tzq_tree = df_tzq_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_tzq_tree = df_tzq_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_tzq = df_tzq_tree.Filter(filters)
  df_tzq_trigger = all_trigger(df_tzq)
  df_tzq_histos=[]
  for i in hists_name:
    df_tzq_histo = df_tzq_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_tzq_histos.append(df_tzq_histo)

  df_Fake_tzq_tree = ROOT.RDataFrame("Events",Fake_tzq_list)
  df_Fake_tzq_tree = df_Fake_tzq_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_tzq_tree = df_Fake_tzq_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_tzq_tree = df_Fake_tzq_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_tzq = df_Fake_tzq_tree.Filter(filters_fake_mc)
  df_Fake_tzq_trigger = all_trigger(df_Fake_tzq)
  df_Fake_tzq_histos=[]
  for i in hists_name:
    df_Fake_tzq_histo = df_Fake_tzq_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_tzq_histos.append(df_Fake_tzq_histo)

  df_TTTo2L_tree = ROOT.RDataFrame("Events",TTTo2L_list)
  df_TTTo2L_tree = df_TTTo2L_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_TTTo2L_tree = df_TTTo2L_tree.Define("genweight","puWeight*PrefireWeight*Electron_RECO_SF[ttc_l1_id]*Electron_RECO_SF[ttc_l2_id]*Electron_CutBased_TightID_SF[ttc_l1_id]*Electron_CutBased_TightID_SF[ttc_l2_id]*trigger_SF*genWeight/abs(genWeight)")
  df_TTTo2L = df_TTTo2L_tree.Filter(filters)
  df_TTTo2L_trigger = all_trigger(df_TTTo2L)
  df_TTTo2L_histos=[]
  for i in hists_name:
    df_TTTo2L_histo = df_TTTo2L_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_TTTo2L_histos.append(df_TTTo2L_histo)

  df_Fake_TTTo2L_tree = ROOT.RDataFrame("Events",Fake_TTTo2L_list)
  df_Fake_TTTo2L_tree = df_Fake_TTTo2L_tree.Define("trigger_SF","trigger_sf_ee(ttc_l1_pt,ttc_l2_pt,ttc_l1_eta,ttc_l2_eta)")
  df_Fake_TTTo2L_tree = df_Fake_TTTo2L_tree.Define("fakelep_weight","fakelepweight_ee_mc(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_Fake_TTTo2L_tree = df_Fake_TTTo2L_tree.Define("genweight","puWeight*PrefireWeight*fakelep_weight*trigger_SF*genWeight/abs(genWeight)")
  df_Fake_TTTo2L = df_Fake_TTTo2L_tree.Filter(filters_fake_mc)
  df_Fake_TTTo2L_trigger = all_trigger(df_Fake_TTTo2L)
  df_Fake_TTTo2L_histos=[]
  for i in hists_name:
    df_Fake_TTTo2L_histo = df_Fake_TTTo2L_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i,'genweight')
    df_Fake_TTTo2L_histos.append(df_Fake_TTTo2L_histo)

  df_DoubleEle_tree = ROOT.RDataFrame("Events", doubleEle_names)
  df_DoubleEle = df_DoubleEle_tree.Filter(filters_data)
  df_DoubleEle_trigger = for_diele_trigger(df_DoubleEle)
  df_DoubleEle_histos=[]
  for i in hists_name:
    df_DoubleEle_histo = df_DoubleEle_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i)
    df_DoubleEle_histos.append(df_DoubleEle_histo)

  df_SingleEle_tree = ROOT.RDataFrame("Events", singleEle_names)
  df_SingleEle = df_SingleEle_tree.Filter(filters_data)
  df_SingleEle_trigger = for_singleele_trigger_eechannel(df_SingleEle)
  df_SingleEle_histos=[]
  for i in hists_name:
    df_SingleEle_histo = df_SingleEle_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i)
    df_SingleEle_histos.append(df_SingleEle_histo)

  df_FakeLep_DoubleEle_tree = ROOT.RDataFrame("Events", FakeLep_doubleEle_names)
  df_FakeLep_DoubleEle_tree = df_FakeLep_DoubleEle_tree.Define("fakelep_weight","fakelepweight_ee_data(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_FakeLep_DoubleEle = df_FakeLep_DoubleEle_tree.Filter(filters_data)
  df_FakeLep_DoubleEle_trigger = for_diele_trigger(df_FakeLep_DoubleEle)
  df_FakeLep_DoubleEle_histos=[]
  for i in hists_name:
    df_FakeLep_DoubleEle_histo = df_FakeLep_DoubleEle_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i, 'fakelep_weight')
    df_FakeLep_DoubleEle_histos.append(df_FakeLep_DoubleEle_histo)

  df_FakeLep_SingleEle_tree = ROOT.RDataFrame("Events", FakeLep_singleEle_names)
  df_FakeLep_SingleEle_tree = df_FakeLep_SingleEle_tree.Define("fakelep_weight","fakelepweight_ee_data(ttc_1P1F,ttc_0P2F,ttc_lep1_faketag,ttc_l1_pt,ttc_l1_eta,ttc_l2_pt,ttc_l2_eta)")
  df_FakeLep_SingleEle = df_FakeLep_SingleEle_tree.Filter(filters_data)
  df_FakeLep_SingleEle_trigger = for_singleele_trigger_eechannel(df_FakeLep_SingleEle)
  df_FakeLep_SingleEle_histos=[]
  for i in hists_name:
    df_FakeLep_SingleEle_histo = df_FakeLep_SingleEle_trigger.Histo1D((i,'',histos_bins[i],histos_bins_low[i],histos_bins_high[i]), i, 'fakelep_weight')
    df_FakeLep_SingleEle_histos.append(df_FakeLep_SingleEle_histo)

  for ij in range(0,len(hists_name)):
    df_DY_histos[ij].Draw()
    df_WW_histos[ij].Draw()
    df_WZ_histos[ij].Draw()
    df_ZZ_histos[ij].Draw()
    df_WWW_histos[ij].Draw()
    df_WWZ_histos[ij].Draw()
    df_WZZ_histos[ij].Draw()
    df_ZZZ_histos[ij].Draw()
    df_tW_histos[ij].Draw()
    df_tbarW_histos[ij].Draw()
    df_ttWtoLNu_histos[ij].Draw()
    df_ttWtoQQ_histos[ij].Draw()
    df_ttZ_histos[ij].Draw()
    df_ttZtoQQ_histos[ij].Draw()
    df_ttH_histos[ij].Draw()
    df_ttWW_histos[ij].Draw()
    df_ttWZ_histos[ij].Draw()
    df_ttZZ_histos[ij].Draw()
    df_tzq_histos[ij].Draw()
    df_TTTo2L_histos[ij].Draw()
    df_DoubleEle_histos[ij].Draw()
    df_SingleEle_histos[ij].Draw()
    df_FakeLep_DoubleEle_histos[ij].Draw()
    df_FakeLep_SingleEle_histos[ij].Draw()
    df_Fake_DY_histos[ij].Draw()
    df_Fake_WW_histos[ij].Draw()
    df_Fake_WZ_histos[ij].Draw()
    df_Fake_ZZ_histos[ij].Draw()
    df_Fake_WWW_histos[ij].Draw()
    df_Fake_WWZ_histos[ij].Draw()
    df_Fake_WZZ_histos[ij].Draw()
    df_Fake_ZZZ_histos[ij].Draw()
    df_Fake_tW_histos[ij].Draw()
    df_Fake_tbarW_histos[ij].Draw()
    df_Fake_ttWtoLNu_histos[ij].Draw()
    df_Fake_ttWtoQQ_histos[ij].Draw()
    df_Fake_ttZ_histos[ij].Draw()
    df_Fake_ttZtoQQ_histos[ij].Draw()
    df_Fake_ttH_histos[ij].Draw()
    df_Fake_ttWW_histos[ij].Draw()
    df_Fake_ttWZ_histos[ij].Draw()
    df_Fake_ttZZ_histos[ij].Draw()
    df_Fake_tzq_histos[ij].Draw()
    df_Fake_TTTo2L_histos[ij].Draw()

# ROOT version 6.14 don;t have function "ROOT.RDF.RunGraphs"
#  ROOT.RDF.RunGraphs({df_ZZG_histo, df_ZZ_histo, df_ggZZ_4e_histo,df_ggZZ_4mu_histo, df_ggZZ_4tau_histo, df_ggZZ_2e2mu_histo,df_ggZZ_2e2tau_histo, df_ggZZ_2mu2tau_histo, df_TTZ_histo,df_TTG_histo, df_WWZ_histo, df_WZG_histo,df_WZZ_histo, df_ZZZ_histo, df_WZTo3L_histo,df_WZTo2L_histo, df_ZG_histo})

    h_DY = df_DY_histos[ij].GetValue()
    h_WW = df_WW_histos[ij].GetValue()
    h_WZ = df_WZ_histos[ij].GetValue()
    h_ZZ = df_ZZ_histos[ij].GetValue()
    h_WWW = df_WWW_histos[ij].GetValue()
    h_WWZ = df_WWZ_histos[ij].GetValue()
    h_WZZ = df_WZZ_histos[ij].GetValue()
    h_ZZZ = df_ZZZ_histos[ij].GetValue()
    h_tW = df_tW_histos[ij].GetValue()
    h_tbarW = df_tbarW_histos[ij].GetValue()
    h_ttWtoLNu = df_ttWtoLNu_histos[ij].GetValue()
    h_ttWtoQQ = df_ttWtoQQ_histos[ij].GetValue()
    h_ttZ = df_ttZ_histos[ij].GetValue()
    h_ttZtoQQ = df_ttZtoQQ_histos[ij].GetValue()
    h_ttH = df_ttH_histos[ij].GetValue()
    h_ttWW = df_ttWW_histos[ij].GetValue()
    h_ttWZ = df_ttWZ_histos[ij].GetValue()
    h_ttZZ = df_ttZZ_histos[ij].GetValue()
    h_tzq = df_tzq_histos[ij].GetValue()
    h_TTTo2L = df_TTTo2L_histos[ij].GetValue()
    h_DoubleEle = df_DoubleEle_histos[ij].GetValue()
    h_SingleEle = df_SingleEle_histos[ij].GetValue()
    h_fakelep_DoubleEle = df_FakeLep_DoubleEle_histos[ij].GetValue()
    h_fakelep_SingleEle = df_FakeLep_SingleEle_histos[ij].GetValue()
    h_fake_DY = df_Fake_DY_histos[ij].GetValue()
    h_fake_WW = df_Fake_WW_histos[ij].GetValue()
    h_fake_WZ = df_Fake_WZ_histos[ij].GetValue()
    h_fake_ZZ = df_Fake_ZZ_histos[ij].GetValue()
    h_fake_WWW = df_Fake_WWW_histos[ij].GetValue()
    h_fake_WWZ = df_Fake_WWZ_histos[ij].GetValue()
    h_fake_WZZ = df_Fake_WZZ_histos[ij].GetValue()
    h_fake_ZZZ = df_Fake_ZZZ_histos[ij].GetValue()
    h_fake_tW = df_Fake_tW_histos[ij].GetValue()
    h_fake_tbarW = df_Fake_tbarW_histos[ij].GetValue()
    h_fake_ttWtoLNu = df_Fake_ttWtoLNu_histos[ij].GetValue()
    h_fake_ttWtoQQ = df_Fake_ttWtoQQ_histos[ij].GetValue()
    h_fake_ttZ = df_Fake_ttZ_histos[ij].GetValue()
    h_fake_ttZtoQQ = df_Fake_ttZtoQQ_histos[ij].GetValue()
    h_fake_ttH = df_Fake_ttH_histos[ij].GetValue()
    h_fake_ttWW = df_Fake_ttWW_histos[ij].GetValue()
    h_fake_ttWZ = df_Fake_ttWZ_histos[ij].GetValue()
    h_fake_ttZZ = df_Fake_ttZZ_histos[ij].GetValue()
    h_fake_tzq = df_Fake_tzq_histos[ij].GetValue()
    h_fake_TTTo2L = df_Fake_TTTo2L_histos[ij].GetValue()

    h_DY.Scale(DY_xs/DY_ev)
    h_WW.Scale(WW_xs/WW_ev)
    h_WZ.Scale(WZ_xs/WZ_ev)
    h_ZZ.Scale(ZZ_xs/ZZ_ev)
    h_WWW.Scale(WWW_xs/WWW_ev)
    h_WWZ.Scale(WWZ_xs/WWZ_ev)
    h_WZZ.Scale(WZZ_xs/WZZ_ev)
    h_ZZZ.Scale(ZZZ_xs/ZZZ_ev)
    h_tW.Scale(tW_xs/tW_ev)
    h_tbarW.Scale(tbarW_xs/tbarW_ev)
    h_ttWtoLNu.Scale(TTWtoLNu_xs/TTWtoLNu_ev)
    h_ttWtoQQ.Scale(TTWtoQQ_xs/TTWtoQQ_ev)
    h_ttZ.Scale(TTZ_xs/TTZ_ev)
    h_ttZtoQQ.Scale(TTZtoQQ_xs/TTZtoQQ_ev)
    h_ttH.Scale(TTH_xs/TTH_ev)
    h_ttWW.Scale(TTWW_xs/TTWW_ev)
    h_ttWZ.Scale(TTWZ_xs/TTWZ_ev)
    h_ttZZ.Scale(TTZZ_xs/TTZZ_ev)
    h_tzq.Scale(tZq_xs/tZq_ev)
    h_TTTo2L.Scale(TTTo2L_xs/TTTo2L_ev)

    h_fake_DY.Scale(DY_xs/Fake_DY_ev)
    h_fake_WW.Scale(WW_xs/Fake_WW_ev)
    h_fake_WZ.Scale(WZ_xs/Fake_WZ_ev)
    h_fake_ZZ.Scale(ZZ_xs/Fake_ZZ_ev)
    h_fake_WWW.Scale(WWW_xs/Fake_WWW_ev)
    h_fake_WWZ.Scale(WWZ_xs/Fake_WWZ_ev)
    h_fake_WZZ.Scale(WZZ_xs/Fake_WZZ_ev)
    h_fake_ZZZ.Scale(ZZZ_xs/Fake_ZZZ_ev)
    h_fake_tW.Scale(tW_xs/Fake_tW_ev)
    h_fake_tbarW.Scale(tbarW_xs/Fake_tbarW_ev)
    h_fake_ttWtoLNu.Scale(TTWtoLNu_xs/Fake_TTWtoLNu_ev)
    h_fake_ttWtoQQ.Scale(TTWtoQQ_xs/Fake_TTWtoQQ_ev)
    h_fake_ttZ.Scale(TTZ_xs/Fake_TTZ_ev)
    h_fake_ttZtoQQ.Scale(TTZtoQQ_xs/Fake_TTZtoQQ_ev)
    h_fake_ttH.Scale(TTH_xs/Fake_TTH_ev)
    h_fake_ttWW.Scale(TTWW_xs/Fake_TTWW_ev)
    h_fake_ttWZ.Scale(TTWZ_xs/Fake_TTWZ_ev)
    h_fake_ttZZ.Scale(TTZZ_xs/Fake_TTZZ_ev)
    h_fake_tzq.Scale(tZq_xs/Fake_tZq_ev)
    h_fake_TTTo2L.Scale(TTTo2L_xs/Fake_TTTo2L_ev)

    histos.append(h_DY.Clone())
    histos.append(h_WW.Clone())
    histos.append(h_WZ.Clone())
    histos.append(h_ZZ.Clone())
    histos.append(h_WWW.Clone())
    histos.append(h_WWZ.Clone())
    histos.append(h_WZZ.Clone())
    histos.append(h_ZZZ.Clone())
    histos.append(h_tW.Clone())
    histos.append(h_tbarW.Clone())
    histos.append(h_ttWtoLNu.Clone())
    histos.append(h_ttWtoQQ.Clone())
    histos.append(h_ttZ.Clone())
    histos.append(h_ttZtoQQ.Clone())
    histos.append(h_ttH.Clone())
    histos.append(h_ttWW.Clone())
    histos.append(h_ttWZ.Clone())
    histos.append(h_ttZZ.Clone())
    histos.append(h_tzq.Clone())
    histos.append(h_TTTo2L.Clone())
    histos.append(h_fake_DY.Clone())
    histos.append(h_fake_WW.Clone())
    histos.append(h_fake_WZ.Clone())
    histos.append(h_fake_ZZ.Clone())
    histos.append(h_fake_WWW.Clone())
    histos.append(h_fake_WWZ.Clone())
    histos.append(h_fake_WZZ.Clone())
    histos.append(h_fake_ZZZ.Clone())
    histos.append(h_fake_tW.Clone())
    histos.append(h_fake_tbarW.Clone())
    histos.append(h_fake_ttWtoLNu.Clone())
    histos.append(h_fake_ttWtoQQ.Clone())
    histos.append(h_fake_ttZ.Clone())
    histos.append(h_fake_ttZtoQQ.Clone())
    histos.append(h_fake_ttH.Clone())
    histos.append(h_fake_ttWW.Clone())
    histos.append(h_fake_ttWZ.Clone())
    histos.append(h_fake_ttZZ.Clone())
    histos.append(h_fake_tzq.Clone())
    histos.append(h_fake_TTTo2L.Clone())
    histos.append(h_fakelep_DoubleEle.Clone())
    histos.append(h_fakelep_SingleEle.Clone())
    histos.append(h_DoubleEle.Clone()) 
    histos.append(h_SingleEle.Clone())

    for i in range(0,44):
      histos[i]=overunder_flowbin(histos[i])

    c1 = plot_TTCregion.draw_plots(histos, 1, hists_name[ij], 0)
    del histos[:]
 
if __name__ == "__main__":
  start = time.time()
  start1 = time.clock() 
  TTC_Analysis()
  end = time.time()
  end1 = time.clock()
  print "wall time:", end-start
  print "process time:", end1-start1
