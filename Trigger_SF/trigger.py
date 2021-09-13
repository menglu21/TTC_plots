import ROOT
import sys
from ROOT import TFile,TTree,TH2D, TH1F, TCanvas,TLegend, TEfficiency, TLorentzVector
from array import array
import math
from math import sqrt

path='/eos/user/m/melu/TTC_Nanov8_new/'
def calc(filename, channel):
  if filename=='B':
    print 'proceeding Data13TeV_2017B_MET.root'
    filein = TFile.Open(path+'METB.root')
    if channel==22:
      fileout=TFile.Open('METB_ee.root','RECREATE')
    elif channel==24:
      fileout=TFile.Open('METB_em.root','RECREATE')
    else:
      fileout=TFile.Open('METB_mm.root','RECREATE')
  elif filename=='C':
    print 'proceeding Data13TeV_2017C_MET.root'
    filein = TFile.Open(path+'METC.root')
    if channel==22:
      fileout=TFile.Open('METC_ee.root','RECREATE')
    elif channel==24:
      fileout=TFile.Open('METC_em.root','RECREATE')
    else:
      fileout=TFile.Open('METC_mm.root','RECREATE')
  elif filename=='D':
    print 'proceeding Data13TeV_2017D_MET.root'
    filein = TFile.Open(path+'METD.root')
    if channel==22:
      fileout=TFile.Open('METD_ee.root','RECREATE')
    elif channel==24:
      fileout=TFile.Open('METD_em.root','RECREATE')
    else:
      fileout=TFile.Open('METD_mm.root','RECREATE')
  elif filename=='E':
    print 'proceeding Data13TeV_2017E_MET.root'
    filein = TFile.Open(path+'METE.root')
    if channel==22:
      fileout=TFile.Open('METE_ee.root','RECREATE')
    elif channel==24:
      fileout=TFile.Open('METE_em.root','RECREATE')
    else:
      fileout=TFile.Open('METE_mm.root','RECREATE')
  elif filename=='F':
    print 'proceeding Data13TeV_2017F_MET.root'
    filein = TFile.Open(path+'METF.root')
    if channel==22:
      fileout=TFile.Open('METF_ee.root','RECREATE')
    elif channel==24:
      fileout=TFile.Open('METF_em.root','RECREATE')
    else:
      fileout=TFile.Open('METF_mm.root','RECREATE')
  elif filename=='ALL':
    print 'proceeding Data13TeV_2017_MET.root'
    filein = TFile.Open(path+'MET.root')
    if channel==22:
      fileout=TFile.Open('MET_ee.root','RECREATE')
    elif channel==24:
      fileout=TFile.Open('MET_em.root','RECREATE')
    else:
      fileout=TFile.Open('MET_mm.root','RECREATE')
  elif filename=='TTto2L':
    print 'proceeding MC13TeV_2017_TTTo2L2Nu.root'
    filein = TFile.Open(path+'TTTo2L.root')
    if channel==22:
      fileout=TFile.Open('TTto2L_ee.root','RECREATE')
    elif channel==24:
      fileout=TFile.Open('TTto2L_em.root','RECREATE')
    else:
      fileout=TFile.Open('TTto2L_mm.root','RECREATE')
  else:
    print 'proceeding MC13TeV_2017_TTToSemiLeptonic.root'
    filein = TFile.Open(path+'TTTo1L.root')
    if channel==22:
      fileout=TFile.Open('TTto1L_ee.root','RECREATE')
    elif channel==24:
      fileout=TFile.Open('TTto1L_em.root','RECREATE')
    else:
      fileout=TFile.Open('TTto1L_mm.root','RECREATE')

  treein = filein.Get('Events')
  
  entries = treein.GetEntries()
  if 'TT' in filename:entries=1500000
  
  l1ptbin=array('d',[20, 40, 50, 65, 80, 100, 200])
  l2ptbin=array('d',[20, 40, 50, 65, 80, 100, 200])
  lepetabin=array('d',[-2.5,-2.1,-1.8,-1.5,-1.2,-0.9,-0.6,-0.3,-0.1,0.1,0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.5])
  jetbin=array('d',[0,1,2,3,4,5,6,7,8,9,10])
  #metbin=array('d',[0,20,40,60,80,100,130,160,200])
  metbin=array('d',[100,110,120,130,140,160,180,200,250])
  tdlepetabin=array('d',[0,0.4,0.9,1.5,2.5])
  tdl1ptbin=array('d',[20,40,50,65,80,100,200])
  tdl2ptbin=array('d',[20,40,50,65,80,100,200])
  
  h1_pre_l1pt = TH1F('pre_l1pt','pre_l1pt',6,l1ptbin)
  h1_pre_l1pt.Sumw2()
  h1_pre_l1pt.SetMinimum(0)
  h1_pre_l1pt.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h1_pre_l1pt.GetYaxis().SetTitle('Efficiency')
  h1_pre_l1pt.SetStats(0)

  h1_pre_l1pt_lowjet = TH1F('pre_l1pt_lowjet','pre_l1pt_lowjet',6,l1ptbin)
  h1_pre_l1pt_lowjet.Sumw2()
  h1_pre_l1pt_lowjet.SetMinimum(0)
  h1_pre_l1pt_lowjet.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h1_pre_l1pt_lowjet.GetYaxis().SetTitle('Efficiency')
  h1_pre_l1pt_lowjet.SetStats(0)

  h1_pre_l1pt_highjet = TH1F('pre_l1pt_highjet','pre_l1pt_highjet',6,l1ptbin)
  h1_pre_l1pt_highjet.Sumw2()
  h1_pre_l1pt_highjet.SetMinimum(0)
  h1_pre_l1pt_highjet.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h1_pre_l1pt_highjet.GetYaxis().SetTitle('Efficiency')
  h1_pre_l1pt_highjet.SetStats(0)

  h1_pre_l1pt_lowpv = TH1F('pre_l1pt_lowpv','pre_l1pt_lowpv',6,l1ptbin)
  h1_pre_l1pt_lowpv.Sumw2()
  h1_pre_l1pt_lowpv.SetMinimum(0)
  h1_pre_l1pt_lowpv.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h1_pre_l1pt_lowpv.GetYaxis().SetTitle('Efficiency')
  h1_pre_l1pt_lowpv.SetStats(0)

  h1_pre_l1pt_highpv = TH1F('pre_l1pt_highpv','pre_l1pt_highpv',6,l1ptbin)
  h1_pre_l1pt_highpv.Sumw2()
  h1_pre_l1pt_highpv.SetMinimum(0)
  h1_pre_l1pt_highpv.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h1_pre_l1pt_highpv.GetYaxis().SetTitle('Efficiency')
  h1_pre_l1pt_highpv.SetStats(0)

  h1_pre_l1pt_lowMET = TH1F('pre_l1pt_lowMET','pre_l1pt_lowMET',6,l1ptbin)
  h1_pre_l1pt_lowMET.Sumw2()
  h1_pre_l1pt_lowMET.SetMinimum(0)
  h1_pre_l1pt_lowMET.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h1_pre_l1pt_lowMET.GetYaxis().SetTitle('Efficiency')
  h1_pre_l1pt_lowMET.SetStats(0)

  h1_pre_l1pt_highMET = TH1F('pre_l1pt_highMET','pre_l1pt_highMET',6,l1ptbin)
  h1_pre_l1pt_highMET.Sumw2()
  h1_pre_l1pt_highMET.SetMinimum(0)
  h1_pre_l1pt_highMET.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h1_pre_l1pt_highMET.GetYaxis().SetTitle('Efficiency')
  h1_pre_l1pt_highMET.SetStats(0)

  h1_pre_l1eta = TH1F('pre_l1eta', 'pre_l1eta',17,lepetabin)
  h1_pre_l1eta.Sumw2()
  h1_pre_l1eta.SetMinimum(0)
  h1_pre_l1eta.GetXaxis().SetTitle('Leading Lepton #eta')
  h1_pre_l1eta.GetYaxis().SetTitle('Efficiency')
  h1_pre_l1eta.SetStats(0)

  h1_pre_l1eta_lowjet = TH1F('pre_l1eta_lowjet', 'pre_l1eta_lowjet',17,lepetabin)
  h1_pre_l1eta_lowjet.Sumw2()
  h1_pre_l1eta_lowjet.SetMinimum(0)
  h1_pre_l1eta_lowjet.GetXaxis().SetTitle('Leading Lepton #eta')
  h1_pre_l1eta_lowjet.GetYaxis().SetTitle('Efficiency')
  h1_pre_l1eta_lowjet.SetStats(0)

  h1_pre_l1eta_highjet = TH1F('pre_l1eta_highjet', 'pre_l1eta_highjet',17,lepetabin)
  h1_pre_l1eta_highjet.Sumw2()
  h1_pre_l1eta_highjet.SetMinimum(0)
  h1_pre_l1eta_highjet.GetXaxis().SetTitle('Leading Lepton #eta')
  h1_pre_l1eta_highjet.GetYaxis().SetTitle('Efficiency')
  h1_pre_l1eta_highjet.SetStats(0)

  h1_pre_l1eta_lowpv = TH1F('pre_l1eta_lowpv', 'pre_l1eta_lowpv',17,lepetabin)
  h1_pre_l1eta_lowpv.Sumw2()
  h1_pre_l1eta_lowpv.SetMinimum(0)
  h1_pre_l1eta_lowpv.GetXaxis().SetTitle('Leading Lepton #eta')
  h1_pre_l1eta_lowpv.GetYaxis().SetTitle('Efficiency')
  h1_pre_l1eta_lowpv.SetStats(0)

  h1_pre_l1eta_highpv = TH1F('pre_l1eta_highpv', 'pre_l1eta_highpv',17,lepetabin)
  h1_pre_l1eta_highpv.Sumw2()
  h1_pre_l1eta_highpv.SetMinimum(0)
  h1_pre_l1eta_highpv.GetXaxis().SetTitle('Leading Lepton #eta')
  h1_pre_l1eta_highpv.GetYaxis().SetTitle('Efficiency')
  h1_pre_l1eta_highpv.SetStats(0)

  h1_pre_l1eta_lowMET = TH1F('pre_l1eta_lowMET', 'pre_l1eta_lowMET',17,lepetabin)
  h1_pre_l1eta_lowMET.Sumw2()
  h1_pre_l1eta_lowMET.SetMinimum(0)
  h1_pre_l1eta_lowMET.GetXaxis().SetTitle('Leading Lepton #eta')
  h1_pre_l1eta_lowMET.GetYaxis().SetTitle('Efficiency')
  h1_pre_l1eta_lowMET.SetStats(0)

  h1_pre_l1eta_highMET = TH1F('pre_l1eta_highMET', 'pre_l1eta_highMET',17,lepetabin)
  h1_pre_l1eta_highMET.Sumw2()
  h1_pre_l1eta_highMET.SetMinimum(0)
  h1_pre_l1eta_highMET.GetXaxis().SetTitle('Leading Lepton #eta')
  h1_pre_l1eta_highMET.GetYaxis().SetTitle('Efficiency')
  h1_pre_l1eta_highMET.SetStats(0)

  h1_pre_l2pt = TH1F('pre_l2pt','pre_l2pt',6,l2ptbin)
  h1_pre_l2pt.Sumw2()
  h1_pre_l2pt.SetMinimum(0)
  h1_pre_l2pt.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h1_pre_l2pt.GetYaxis().SetTitle('Efficiency')
  h1_pre_l2pt.SetStats(0)

  h1_pre_l2pt_lowjet = TH1F('pre_l2pt_lowjet','pre_l2pt_lowjet',6,l2ptbin)
  h1_pre_l2pt_lowjet.Sumw2()
  h1_pre_l2pt_lowjet.SetMinimum(0)
  h1_pre_l2pt_lowjet.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h1_pre_l2pt_lowjet.GetYaxis().SetTitle('Efficiency')
  h1_pre_l2pt_lowjet.SetStats(0)

  h1_pre_l2pt_highjet = TH1F('pre_l2pt_highjet','pre_l2pt_highjet',6,l2ptbin)
  h1_pre_l2pt_highjet.Sumw2()
  h1_pre_l2pt_highjet.SetMinimum(0)
  h1_pre_l2pt_highjet.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h1_pre_l2pt_highjet.GetYaxis().SetTitle('Efficiency')
  h1_pre_l2pt_highjet.SetStats(0)

  h1_pre_l2pt_lowpv = TH1F('pre_l2pt_lowpv','pre_l2pt_lowpv',6,l2ptbin)
  h1_pre_l2pt_lowpv.Sumw2()
  h1_pre_l2pt_lowpv.SetMinimum(0)
  h1_pre_l2pt_lowpv.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h1_pre_l2pt_lowpv.GetYaxis().SetTitle('Efficiency')
  h1_pre_l2pt_lowpv.SetStats(0)

  h1_pre_l2pt_highpv = TH1F('pre_l2pt_highpv','pre_l2pt_highpv',6,l2ptbin)
  h1_pre_l2pt_highpv.Sumw2()
  h1_pre_l2pt_highpv.SetMinimum(0)
  h1_pre_l2pt_highpv.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h1_pre_l2pt_highpv.GetYaxis().SetTitle('Efficiency')
  h1_pre_l2pt_highpv.SetStats(0)

  h1_pre_l2pt_lowMET = TH1F('pre_l2pt_lowMET','pre_l2pt_lowMET',6,l2ptbin)
  h1_pre_l2pt_lowMET.Sumw2()
  h1_pre_l2pt_lowMET.SetMinimum(0)
  h1_pre_l2pt_lowMET.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h1_pre_l2pt_lowMET.GetYaxis().SetTitle('Efficiency')
  h1_pre_l2pt_lowMET.SetStats(0)

  h1_pre_l2pt_highMET = TH1F('pre_l2pt_highMET','pre_l2pt_highMET',6,l2ptbin)
  h1_pre_l2pt_highMET.Sumw2()
  h1_pre_l2pt_highMET.SetMinimum(0)
  h1_pre_l2pt_highMET.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h1_pre_l2pt_highMET.GetYaxis().SetTitle('Efficiency')
  h1_pre_l2pt_highMET.SetStats(0)

  h1_pre_l2eta = TH1F('pre_l2eta', 'pre_l2eta',17,lepetabin)
  h1_pre_l2eta.Sumw2()
  h1_pre_l2eta.SetMinimum(0)
  h1_pre_l2eta.GetXaxis().SetTitle('Subleading Lepton #eta')
  h1_pre_l2eta.GetYaxis().SetTitle('Efficiency')
  h1_pre_l2eta.SetStats(0)

  h1_pre_l2eta_lowjet = TH1F('pre_l2eta_lowjet', 'pre_l2eta_lowjet',17,lepetabin)
  h1_pre_l2eta_lowjet.Sumw2()
  h1_pre_l2eta_lowjet.SetMinimum(0)
  h1_pre_l2eta_lowjet.GetXaxis().SetTitle('Subleading Lepton #eta')
  h1_pre_l2eta_lowjet.GetYaxis().SetTitle('Efficiency')
  h1_pre_l2eta_lowjet.SetStats(0)

  h1_pre_l2eta_highjet = TH1F('pre_l2eta_highjet', 'pre_l2eta_highjet',17,lepetabin)
  h1_pre_l2eta_highjet.Sumw2()
  h1_pre_l2eta_highjet.SetMinimum(0)
  h1_pre_l2eta_highjet.GetXaxis().SetTitle('Subleading Lepton #eta')
  h1_pre_l2eta_highjet.GetYaxis().SetTitle('Efficiency')
  h1_pre_l2eta_highjet.SetStats(0)

  h1_pre_l2eta_lowpv = TH1F('pre_l2eta_lowpv', 'pre_l2eta_lowpv',17,lepetabin)
  h1_pre_l2eta_lowpv.Sumw2()
  h1_pre_l2eta_lowpv.SetMinimum(0)
  h1_pre_l2eta_lowpv.GetXaxis().SetTitle('Subleading Lepton #eta')
  h1_pre_l2eta_lowpv.GetYaxis().SetTitle('Efficiency')
  h1_pre_l2eta_lowpv.SetStats(0)

  h1_pre_l2eta_highpv = TH1F('pre_l2eta_highpv', 'pre_l2eta_highpv',17,lepetabin)
  h1_pre_l2eta_highpv.Sumw2()
  h1_pre_l2eta_highpv.SetMinimum(0)
  h1_pre_l2eta_highpv.GetXaxis().SetTitle('Subleading Lepton #eta')
  h1_pre_l2eta_highpv.GetYaxis().SetTitle('Efficiency')
  h1_pre_l2eta_highpv.SetStats(0)

  h1_pre_l2eta_lowMET = TH1F('pre_l2eta_lowMET', 'pre_l2eta_lowMET',17,lepetabin)
  h1_pre_l2eta_lowMET.Sumw2()
  h1_pre_l2eta_lowMET.SetMinimum(0)
  h1_pre_l2eta_lowMET.GetXaxis().SetTitle('Subleading Lepton #eta')
  h1_pre_l2eta_lowMET.GetYaxis().SetTitle('Efficiency')
  h1_pre_l2eta_lowMET.SetStats(0)

  h1_pre_l2eta_highMET = TH1F('pre_l2eta_highMET', 'pre_l2eta_highMET',17,lepetabin)
  h1_pre_l2eta_highMET.Sumw2()
  h1_pre_l2eta_highMET.SetMinimum(0)
  h1_pre_l2eta_highMET.GetXaxis().SetTitle('Subleading Lepton #eta')
  h1_pre_l2eta_highMET.GetYaxis().SetTitle('Efficiency')
  h1_pre_l2eta_highMET.SetStats(0)

  h1_pre_njet = TH1F('pre_njet', 'pre_njet', 9, jetbin)
  h1_pre_njet.Sumw2()
  h1_pre_njet.SetMinimum(0)
  h1_pre_njet.GetXaxis().SetTitle('N_{jets}')
  h1_pre_njet.GetYaxis().SetTitle('Efficiency')
  h1_pre_njet.SetStats(0)

  h1_pre_njet_lowpv = TH1F('pre_njet_lowpv', 'pre_njet_lowpv', 9, jetbin)
  h1_pre_njet_lowpv.Sumw2()
  h1_pre_njet_lowpv.SetMinimum(0)
  h1_pre_njet_lowpv.GetXaxis().SetTitle('N_{jets}')
  h1_pre_njet_lowpv.GetYaxis().SetTitle('Efficiency')
  h1_pre_njet_lowpv.SetStats(0)

  h1_pre_njet_highpv = TH1F('pre_njet_highpv', 'pre_njet_highpv', 9, jetbin)
  h1_pre_njet_highpv.Sumw2()
  h1_pre_njet_highpv.SetMinimum(0)
  h1_pre_njet_highpv.GetXaxis().SetTitle('N_{jets}')
  h1_pre_njet_highpv.GetYaxis().SetTitle('Efficiency')
  h1_pre_njet_highpv.SetStats(0)

  h1_pre_njet_lowMET = TH1F('pre_njet_lowMET', 'pre_njet_lowMET', 9, jetbin)
  h1_pre_njet_lowMET.Sumw2()
  h1_pre_njet_lowMET.SetMinimum(0)
  h1_pre_njet_lowMET.GetXaxis().SetTitle('N_{jets}')
  h1_pre_njet_lowMET.GetYaxis().SetTitle('Efficiency')
  h1_pre_njet_lowMET.SetStats(0)

  h1_pre_njet_highMET = TH1F('pre_njet_highMET', 'pre_njet_highMET', 9, jetbin)
  h1_pre_njet_highMET.Sumw2()
  h1_pre_njet_highMET.SetMinimum(0)
  h1_pre_njet_highMET.GetXaxis().SetTitle('N_{jets}')
  h1_pre_njet_highMET.GetYaxis().SetTitle('Efficiency')
  h1_pre_njet_highMET.SetStats(0)

  h1_pre_met = TH1F('pre_met', 'pre_met', 8, metbin)
  h1_pre_met.Sumw2()
  h1_pre_met.SetMinimum(0)
  h1_pre_met.GetXaxis().SetTitle('MET [GeV]')
  h1_pre_met.GetYaxis().SetTitle('Efficiency')
  h1_pre_met.SetStats(0)

  h1_pre_met_lowjet = TH1F('pre_met_lowjet', 'pre_met_lowjet', 8, metbin)
  h1_pre_met_lowjet.Sumw2()
  h1_pre_met_lowjet.SetMinimum(0)
  h1_pre_met_lowjet.GetXaxis().SetTitle('MET [GeV]')
  h1_pre_met_lowjet.GetYaxis().SetTitle('Efficiency')
  h1_pre_met_lowjet.SetStats(0)

  h1_pre_met_highjet = TH1F('pre_met_highjet', 'pre_met_highjet', 8, metbin)
  h1_pre_met_highjet.Sumw2()
  h1_pre_met_highjet.SetMinimum(0)
  h1_pre_met_highjet.GetXaxis().SetTitle('MET [GeV]')
  h1_pre_met_highjet.GetYaxis().SetTitle('Efficiency')
  h1_pre_met_highjet.SetStats(0)

  h1_pre_met_lowpv = TH1F('pre_met_lowpv', 'pre_met_lowpv', 8, metbin)
  h1_pre_met_lowpv.Sumw2()
  h1_pre_met_lowpv.SetMinimum(0)
  h1_pre_met_lowpv.GetXaxis().SetTitle('MET [GeV]')
  h1_pre_met_lowpv.GetYaxis().SetTitle('Efficiency')
  h1_pre_met_lowpv.SetStats(0)

  h1_pre_met_highpv = TH1F('pre_met_highpv', 'pre_met_highpv', 8, metbin)
  h1_pre_met_highpv.Sumw2()
  h1_pre_met_highpv.SetMinimum(0)
  h1_pre_met_highpv.GetXaxis().SetTitle('MET [GeV]')
  h1_pre_met_highpv.GetYaxis().SetTitle('Efficiency')
  h1_pre_met_highpv.SetStats(0)

  h1_pre_pu = TH1F('pre_pu', 'pre_pu',40, 0, 80)
  h1_pre_pu.Sumw2()
  h1_pre_pu.SetMinimum(0)
  h1_pre_pu.SetStats(0)

  h1_pre_putrue = TH1F('pre_putrue', 'pre_putrue',40, 0, 80)
  h1_pre_putrue.Sumw2()
  h1_pre_putrue.SetMinimum(0)
  h1_pre_putrue.SetStats(0)

  h2_pre_l1pteta = TH2D('pre_l1pteta', 'pre_l1pteta', 6,tdl1ptbin,4,tdlepetabin)
  h2_pre_l1pteta.Sumw2()
  h2_pre_l1pteta.SetStats(0)
  h2_pre_l1pteta.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_pre_l1pteta.GetYaxis().SetTitle('Leading Lepton #||{#eta}')

  h2_pre_l1pteta_lowjet = TH2D('pre_l1pteta_lowjet', 'pre_l1pteta_lowjet', 6,tdl1ptbin,4,tdlepetabin)
  h2_pre_l1pteta_lowjet.Sumw2()
  h2_pre_l1pteta_lowjet.SetStats(0)
  h2_pre_l1pteta_lowjet.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_pre_l1pteta_lowjet.GetYaxis().SetTitle('Leading Lepton #||{#eta}')

  h2_pre_l1pteta_highjet = TH2D('pre_l1pteta_highjet', 'pre_l1pteta_highjet', 6,tdl1ptbin,4,tdlepetabin)
  h2_pre_l1pteta_highjet.Sumw2()
  h2_pre_l1pteta_highjet.SetStats(0)
  h2_pre_l1pteta_highjet.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_pre_l1pteta_highjet.GetYaxis().SetTitle('Leading Lepton #||{#eta}')

  h2_pre_l1pteta_lowpv = TH2D('pre_l1pteta_lowpv', 'pre_l1pteta_lowpv', 6,tdl1ptbin,4,tdlepetabin)
  h2_pre_l1pteta_lowpv.Sumw2()
  h2_pre_l1pteta_lowpv.SetStats(0)
  h2_pre_l1pteta_lowpv.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_pre_l1pteta_lowpv.GetYaxis().SetTitle('Leading Lepton #||{#eta}')

  h2_pre_l1pteta_highpv = TH2D('pre_l1pteta_highpv', 'pre_l1pteta_highpv', 6,tdl1ptbin,4,tdlepetabin)
  h2_pre_l1pteta_highpv.Sumw2()
  h2_pre_l1pteta_highpv.SetStats(0)
  h2_pre_l1pteta_highpv.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_pre_l1pteta_highpv.GetYaxis().SetTitle('Leading Lepton #||{#eta}')

  h2_pre_l1pteta_lowMET = TH2D('pre_l1pteta_lowMET', 'pre_l1pteta_lowMET', 6,tdl1ptbin,4,tdlepetabin)
  h2_pre_l1pteta_lowMET.Sumw2()
  h2_pre_l1pteta_lowMET.SetStats(0)
  h2_pre_l1pteta_lowMET.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_pre_l1pteta_lowMET.GetYaxis().SetTitle('Leading Lepton #||{#eta}')

  h2_pre_l1pteta_highMET = TH2D('pre_l1pteta_highMET', 'pre_l1pteta_highMET', 6,tdl1ptbin,4,tdlepetabin)
  h2_pre_l1pteta_highMET.Sumw2()
  h2_pre_l1pteta_highMET.SetStats(0)
  h2_pre_l1pteta_highMET.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_pre_l1pteta_highMET.GetYaxis().SetTitle('Leading Lepton #||{#eta}')

  h2_pre_l2pteta = TH2D('pre_l2pteta', 'pre_l2pteta', 6,tdl1ptbin,4,tdlepetabin)
  h2_pre_l2pteta.Sumw2()
  h2_pre_l2pteta.SetStats(0)
  h2_pre_l2pteta.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_pre_l2pteta.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')

  h2_pre_l2pteta_lowjet = TH2D('pre_l2pteta_lowjet', 'pre_l2pteta_lowjet', 6,tdl1ptbin,4,tdlepetabin)
  h2_pre_l2pteta_lowjet.Sumw2()
  h2_pre_l2pteta_lowjet.SetStats(0)
  h2_pre_l2pteta_lowjet.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_pre_l2pteta_lowjet.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')

  h2_pre_l2pteta_highjet = TH2D('pre_l2pteta_highjet', 'pre_l2pteta_highjet', 6,tdl1ptbin,4,tdlepetabin)
  h2_pre_l2pteta_highjet.Sumw2()
  h2_pre_l2pteta_highjet.SetStats(0)
  h2_pre_l2pteta_highjet.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_pre_l2pteta_highjet.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')

  h2_pre_l2pteta_lowpv = TH2D('pre_l2pteta_lowpv', 'pre_l2pteta_lowpv', 6,tdl1ptbin,4,tdlepetabin)
  h2_pre_l2pteta_lowpv.Sumw2()
  h2_pre_l2pteta_lowpv.SetStats(0)
  h2_pre_l2pteta_lowpv.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_pre_l2pteta_lowpv.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')

  h2_pre_l2pteta_highpv = TH2D('pre_l2pteta_highpv', 'pre_l2pteta_highpv', 6,tdl1ptbin,4,tdlepetabin)
  h2_pre_l2pteta_highpv.Sumw2()
  h2_pre_l2pteta_highpv.SetStats(0)
  h2_pre_l2pteta_highpv.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_pre_l2pteta_highpv.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')

  h2_pre_l2pteta_lowMET = TH2D('pre_l2pteta_lowMET', 'pre_l2pteta_lowMET', 6,tdl1ptbin,4,tdlepetabin)
  h2_pre_l2pteta_lowMET.Sumw2()
  h2_pre_l2pteta_lowMET.SetStats(0)
  h2_pre_l2pteta_lowMET.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_pre_l2pteta_lowMET.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')

  h2_pre_l2pteta_highMET = TH2D('pre_l2pteta_highMET', 'pre_l2pteta_highMET', 6,tdl1ptbin,4,tdlepetabin)
  h2_pre_l2pteta_highMET.Sumw2()
  h2_pre_l2pteta_highMET.SetStats(0)
  h2_pre_l2pteta_highMET.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_pre_l2pteta_highMET.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')

  h2_pre_l1l2pt = TH2D('pre_l1l2pt', 'pre_l1l2pt', 6, tdl1ptbin, 6, tdl2ptbin)
  h2_pre_l1l2pt.Sumw2()
  h2_pre_l1l2pt.SetStats(0)
  h2_pre_l1l2pt.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_pre_l1l2pt.GetYaxis().SetTitle('Subleading Lepton P_{T} [GeV]')

  h2_pre_l1l2pt_lowjet = TH2D('pre_l1l2pt_lowjet', 'pre_l1l2pt_lowjet', 6, tdl1ptbin, 6, tdl2ptbin)
  h2_pre_l1l2pt_lowjet.Sumw2()
  h2_pre_l1l2pt_lowjet.SetStats(0)
  h2_pre_l1l2pt_lowjet.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_pre_l1l2pt_lowjet.GetYaxis().SetTitle('Subleading Lepton P_{T} [GeV]')

  h2_pre_l1l2pt_highjet = TH2D('pre_l1l2pt_highjet', 'pre_l1l2pt_highjet', 6, tdl1ptbin, 6, tdl2ptbin)
  h2_pre_l1l2pt_highjet.Sumw2()
  h2_pre_l1l2pt_highjet.SetStats(0)
  h2_pre_l1l2pt_highjet.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_pre_l1l2pt_highjet.GetYaxis().SetTitle('Subleading Lepton P_{T} [GeV]')

  h2_pre_l1l2pt_lowpv = TH2D('pre_l1l2pt_lowpv', 'pre_l1l2pt_lowpv', 6, tdl1ptbin, 6, tdl2ptbin)
  h2_pre_l1l2pt_lowpv.Sumw2()
  h2_pre_l1l2pt_lowpv.SetStats(0)
  h2_pre_l1l2pt_lowpv.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_pre_l1l2pt_lowpv.GetYaxis().SetTitle('Subleading Lepton P_{T} [GeV]')

  h2_pre_l1l2pt_highpv = TH2D('pre_l1l2pt_highpv', 'pre_l1l2pt_highpv', 6, tdl1ptbin, 6, tdl2ptbin)
  h2_pre_l1l2pt_highpv.Sumw2()
  h2_pre_l1l2pt_highpv.SetStats(0)
  h2_pre_l1l2pt_highpv.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_pre_l1l2pt_highpv.GetYaxis().SetTitle('Subleading Lepton P_{T} [GeV]')

  h2_pre_l1l2pt_lowMET = TH2D('pre_l1l2pt_lowMET', 'pre_l1l2pt_lowMET', 6, tdl1ptbin, 6, tdl2ptbin)
  h2_pre_l1l2pt_lowMET.Sumw2()
  h2_pre_l1l2pt_lowMET.SetStats(0)
  h2_pre_l1l2pt_lowMET.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_pre_l1l2pt_lowMET.GetYaxis().SetTitle('Subleading Lepton P_{T} [GeV]')

  h2_pre_l1l2pt_highMET = TH2D('pre_l1l2pt_highMET', 'pre_l1l2pt_highMET', 6, tdl1ptbin, 6, tdl2ptbin)
  h2_pre_l1l2pt_highMET.Sumw2()
  h2_pre_l1l2pt_highMET.SetStats(0)
  h2_pre_l1l2pt_highMET.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_pre_l1l2pt_highMET.GetYaxis().SetTitle('Subleading Lepton P_{T} [GeV]')

  h2_pre_l1l2eta = TH2D('pre_l1l2eta','pre_l1l2eta',4,tdlepetabin,4,tdlepetabin)
  h2_pre_l1l2eta.Sumw2()
  h2_pre_l1l2eta.GetXaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_pre_l1l2eta.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_pre_l1l2eta.SetStats(0)
  
  h2_pre_l1l2eta_lowjet = TH2D('pre_l1l2eta_lowjet','pre_l1l2eta_lowjet',4,tdlepetabin,4,tdlepetabin)
  h2_pre_l1l2eta_lowjet.Sumw2()
  h2_pre_l1l2eta_lowjet.GetXaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_pre_l1l2eta_lowjet.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_pre_l1l2eta_lowjet.SetStats(0)

  h2_pre_l1l2eta_highjet = TH2D('pre_l1l2eta_highjet','pre_l1l2eta_highjet',4,tdlepetabin,4,tdlepetabin)
  h2_pre_l1l2eta_highjet.Sumw2()
  h2_pre_l1l2eta_highjet.GetXaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_pre_l1l2eta_highjet.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_pre_l1l2eta_highjet.SetStats(0)
  
  h2_pre_l1l2eta_lowpv = TH2D('pre_l1l2eta_lowpv','pre_l1l2eta_lowpv',4,tdlepetabin,4,tdlepetabin)
  h2_pre_l1l2eta_lowpv.Sumw2()
  h2_pre_l1l2eta_lowpv.GetXaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_pre_l1l2eta_lowpv.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_pre_l1l2eta_lowpv.SetStats(0)

  h2_pre_l1l2eta_highpv = TH2D('pre_l1l2eta_highpv','pre_l1l2eta_highpv',4,tdlepetabin,4,tdlepetabin)
  h2_pre_l1l2eta_highpv.Sumw2()
  h2_pre_l1l2eta_highpv.GetXaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_pre_l1l2eta_highpv.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_pre_l1l2eta_highpv.SetStats(0)
  
  h2_pre_l1l2eta_lowMET = TH2D('pre_l1l2eta_lowMET','pre_l1l2eta_lowMET',4,tdlepetabin,4,tdlepetabin)
  h2_pre_l1l2eta_lowMET.Sumw2()
  h2_pre_l1l2eta_lowMET.GetXaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_pre_l1l2eta_lowMET.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_pre_l1l2eta_lowMET.SetStats(0)

  h2_pre_l1l2eta_highMET = TH2D('pre_l1l2eta_highMET','pre_l1l2eta_highMET',4,tdlepetabin,4,tdlepetabin)
  h2_pre_l1l2eta_highMET.Sumw2()
  h2_pre_l1l2eta_highMET.GetXaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_pre_l1l2eta_highMET.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_pre_l1l2eta_highMET.SetStats(0)
  
  h1_l1pt = TH1F('l1pt','l1pt',6,l1ptbin)
  h1_l1pt.Sumw2()
  h1_l1pt.SetMinimum(0)
  h1_l1pt.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h1_l1pt.GetYaxis().SetTitle('Efficiency')
  h1_l1pt.SetStats(0)

  h1_l1pt_lowjet = TH1F('l1pt_lowjet','l1pt_lowjet',6,l1ptbin)
  h1_l1pt_lowjet.Sumw2()
  h1_l1pt_lowjet.SetMinimum(0)
  h1_l1pt_lowjet.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h1_l1pt_lowjet.GetYaxis().SetTitle('Efficiency')
  h1_l1pt_lowjet.SetStats(0)

  h1_l1pt_highjet = TH1F('l1pt_highjet','l1pt_highjet',6,l1ptbin)
  h1_l1pt_highjet.Sumw2()
  h1_l1pt_highjet.SetMinimum(0)
  h1_l1pt_highjet.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h1_l1pt_highjet.GetYaxis().SetTitle('Efficiency')
  h1_l1pt_highjet.SetStats(0)

  h1_l1pt_lowpv = TH1F('l1pt_lowpv','l1pt_lowpv',6,l1ptbin)
  h1_l1pt_lowpv.Sumw2()
  h1_l1pt_lowpv.SetMinimum(0)
  h1_l1pt_lowpv.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h1_l1pt_lowpv.GetYaxis().SetTitle('Efficiency')
  h1_l1pt_lowpv.SetStats(0)

  h1_l1pt_highpv = TH1F('l1pt_highpv','l1pt_highpv',6,l1ptbin)
  h1_l1pt_highpv.Sumw2()
  h1_l1pt_highpv.SetMinimum(0)
  h1_l1pt_highpv.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h1_l1pt_highpv.GetYaxis().SetTitle('Efficiency')
  h1_l1pt_highpv.SetStats(0)

  h1_l1pt_lowMET = TH1F('l1pt_lowMET','l1pt_lowMET',6,l1ptbin)
  h1_l1pt_lowMET.Sumw2()
  h1_l1pt_lowMET.SetMinimum(0)
  h1_l1pt_lowMET.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h1_l1pt_lowMET.GetYaxis().SetTitle('Efficiency')
  h1_l1pt_lowMET.SetStats(0)

  h1_l1pt_highMET = TH1F('l1pt_highMET','l1pt_highMET',6,l1ptbin)
  h1_l1pt_highMET.Sumw2()
  h1_l1pt_highMET.SetMinimum(0)
  h1_l1pt_highMET.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h1_l1pt_highMET.GetYaxis().SetTitle('Efficiency')
  h1_l1pt_highMET.SetStats(0)

  h1_l1eta = TH1F('l1eta', 'l1eta',17,lepetabin)
  h1_l1eta.Sumw2()
  h1_l1eta.SetMinimum(0)
  h1_l1eta.GetXaxis().SetTitle('Leading Lepton #eta')
  h1_l1eta.GetYaxis().SetTitle('Efficiency')
  h1_l1eta.SetStats(0)

  h1_l1eta_lowjet = TH1F('l1eta_lowjet', 'l1eta_lowjet',17,lepetabin)
  h1_l1eta_lowjet.Sumw2()
  h1_l1eta_lowjet.SetMinimum(0)
  h1_l1eta_lowjet.GetXaxis().SetTitle('Leading Lepton #eta')
  h1_l1eta_lowjet.GetYaxis().SetTitle('Efficiency')
  h1_l1eta_lowjet.SetStats(0)

  h1_l1eta_highjet = TH1F('l1eta_highjet', 'l1eta_highjet',17,lepetabin)
  h1_l1eta_highjet.Sumw2()
  h1_l1eta_highjet.SetMinimum(0)
  h1_l1eta_highjet.GetXaxis().SetTitle('Leading Lepton #eta')
  h1_l1eta_highjet.GetYaxis().SetTitle('Efficiency')
  h1_l1eta_highjet.SetStats(0)

  h1_l1eta_lowpv = TH1F('l1eta_lowpv', 'l1eta_lowpv',17,lepetabin)
  h1_l1eta_lowpv.Sumw2()
  h1_l1eta_lowpv.SetMinimum(0)
  h1_l1eta_lowpv.GetXaxis().SetTitle('Leading Lepton #eta')
  h1_l1eta_lowpv.GetYaxis().SetTitle('Efficiency')
  h1_l1eta_lowpv.SetStats(0)

  h1_l1eta_highpv = TH1F('l1eta_highpv', 'l1eta_highpv',17,lepetabin)
  h1_l1eta_highpv.Sumw2()
  h1_l1eta_highpv.SetMinimum(0)
  h1_l1eta_highpv.GetXaxis().SetTitle('Leading Lepton #eta')
  h1_l1eta_highpv.GetYaxis().SetTitle('Efficiency')
  h1_l1eta_highpv.SetStats(0)

  h1_l1eta_lowMET = TH1F('l1eta_lowMET', 'l1eta_lowMET',17,lepetabin)
  h1_l1eta_lowMET.Sumw2()
  h1_l1eta_lowMET.SetMinimum(0)
  h1_l1eta_lowMET.GetXaxis().SetTitle('Leading Lepton #eta')
  h1_l1eta_lowMET.GetYaxis().SetTitle('Efficiency')
  h1_l1eta_lowMET.SetStats(0)

  h1_l1eta_highMET = TH1F('l1eta_highMET', 'l1eta_highMET',17,lepetabin)
  h1_l1eta_highMET.Sumw2()
  h1_l1eta_highMET.SetMinimum(0)
  h1_l1eta_highMET.GetXaxis().SetTitle('Leading Lepton #eta')
  h1_l1eta_highMET.GetYaxis().SetTitle('Efficiency')
  h1_l1eta_highMET.SetStats(0)

  h1_l2pt = TH1F('l2pt','l2pt',6,l2ptbin)
  h1_l2pt.Sumw2()
  h1_l2pt.SetMinimum(0)
  h1_l2pt.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h1_l2pt.GetYaxis().SetTitle('Efficiency')
  h1_l2pt.SetStats(0)

  h1_l2pt_lowjet = TH1F('l2pt_lowjet','l2pt_lowjet',6,l2ptbin)
  h1_l2pt_lowjet.Sumw2()
  h1_l2pt_lowjet.SetMinimum(0)
  h1_l2pt_lowjet.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h1_l2pt_lowjet.GetYaxis().SetTitle('Efficiency')
  h1_l2pt_lowjet.SetStats(0)

  h1_l2pt_highjet = TH1F('l2pt_highjet','l2pt_highjet',6,l2ptbin)
  h1_l2pt_highjet.Sumw2()
  h1_l2pt_highjet.SetMinimum(0)
  h1_l2pt_highjet.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h1_l2pt_highjet.GetYaxis().SetTitle('Efficiency')
  h1_l2pt_highjet.SetStats(0)

  h1_l2pt_lowpv = TH1F('l2pt_lowpv','l2pt_lowpv',6,l2ptbin)
  h1_l2pt_lowpv.Sumw2()
  h1_l2pt_lowpv.SetMinimum(0)
  h1_l2pt_lowpv.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h1_l2pt_lowpv.GetYaxis().SetTitle('Efficiency')
  h1_l2pt_lowpv.SetStats(0)

  h1_l2pt_highpv = TH1F('l2pt_highpv','l2pt_highpv',6,l2ptbin)
  h1_l2pt_highpv.Sumw2()
  h1_l2pt_highpv.SetMinimum(0)
  h1_l2pt_highpv.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h1_l2pt_highpv.GetYaxis().SetTitle('Efficiency')
  h1_l2pt_highpv.SetStats(0)

  h1_l2pt_lowMET = TH1F('l2pt_lowMET','l2pt_lowMET',6,l2ptbin)
  h1_l2pt_lowMET.Sumw2()
  h1_l2pt_lowMET.SetMinimum(0)
  h1_l2pt_lowMET.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h1_l2pt_lowMET.GetYaxis().SetTitle('Efficiency')
  h1_l2pt_lowMET.SetStats(0)

  h1_l2pt_highMET = TH1F('l2pt_highMET','l2pt_highMET',6,l2ptbin)
  h1_l2pt_highMET.Sumw2()
  h1_l2pt_highMET.SetMinimum(0)
  h1_l2pt_highMET.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h1_l2pt_highMET.GetYaxis().SetTitle('Efficiency')
  h1_l2pt_highMET.SetStats(0)

  h1_l2eta = TH1F('l2eta', 'l2eta',17,lepetabin)
  h1_l2eta.Sumw2()
  h1_l2eta.SetMinimum(0)
  h1_l2eta.GetXaxis().SetTitle('Subleading Lepton #eta')
  h1_l2eta.GetYaxis().SetTitle('Efficiency')
  h1_l2eta.SetStats(0)

  h1_l2eta_lowjet = TH1F('l2eta_lowjet', 'l2eta_lowjet',17,lepetabin)
  h1_l2eta_lowjet.Sumw2()
  h1_l2eta_lowjet.SetMinimum(0)
  h1_l2eta_lowjet.GetXaxis().SetTitle('Subleading Lepton #eta')
  h1_l2eta_lowjet.GetYaxis().SetTitle('Efficiency')
  h1_l2eta_lowjet.SetStats(0)

  h1_l2eta_highjet = TH1F('l2eta_highjet', 'l2eta_highjet',17,lepetabin)
  h1_l2eta_highjet.Sumw2()
  h1_l2eta_highjet.SetMinimum(0)
  h1_l2eta_highjet.GetXaxis().SetTitle('Subleading Lepton #eta')
  h1_l2eta_highjet.GetYaxis().SetTitle('Efficiency')
  h1_l2eta_highjet.SetStats(0)

  h1_l2eta_lowpv = TH1F('l2eta_lowpv', 'l2eta_lowpv',17,lepetabin)
  h1_l2eta_lowpv.Sumw2()
  h1_l2eta_lowpv.SetMinimum(0)
  h1_l2eta_lowpv.GetXaxis().SetTitle('Subleading Lepton #eta')
  h1_l2eta_lowpv.GetYaxis().SetTitle('Efficiency')
  h1_l2eta_lowpv.SetStats(0)

  h1_l2eta_highpv = TH1F('l2eta_highpv', 'l2eta_highpv',17,lepetabin)
  h1_l2eta_highpv.Sumw2()
  h1_l2eta_highpv.SetMinimum(0)
  h1_l2eta_highpv.GetXaxis().SetTitle('Subleading Lepton #eta')
  h1_l2eta_highpv.GetYaxis().SetTitle('Efficiency')
  h1_l2eta_highpv.SetStats(0)

  h1_l2eta_lowMET = TH1F('l2eta_lowMET', 'l2eta_lowMET',17,lepetabin)
  h1_l2eta_lowMET.Sumw2()
  h1_l2eta_lowMET.SetMinimum(0)
  h1_l2eta_lowMET.GetXaxis().SetTitle('Subleading Lepton #eta')
  h1_l2eta_lowMET.GetYaxis().SetTitle('Efficiency')
  h1_l2eta_lowMET.SetStats(0)

  h1_l2eta_highMET = TH1F('l2eta_highMET', 'l2eta_highMET',17,lepetabin)
  h1_l2eta_highMET.Sumw2()
  h1_l2eta_highMET.SetMinimum(0)
  h1_l2eta_highMET.GetXaxis().SetTitle('Subleading Lepton #eta')
  h1_l2eta_highMET.GetYaxis().SetTitle('Efficiency')
  h1_l2eta_highMET.SetStats(0)

  h1_njet = TH1F('njet', 'njet', 9, jetbin)
  h1_njet.Sumw2()
  h1_njet.SetMinimum(0)
  h1_njet.GetXaxis().SetTitle('N_{jets}')
  h1_njet.GetYaxis().SetTitle('Efficiency')
  h1_njet.SetStats(0)

  h1_njet_lowpv = TH1F('njet_lowpv', 'njet_lowpv', 9, jetbin)
  h1_njet_lowpv.Sumw2()
  h1_njet_lowpv.SetMinimum(0)
  h1_njet_lowpv.GetXaxis().SetTitle('N_{jets}')
  h1_njet_lowpv.GetYaxis().SetTitle('Efficiency')
  h1_njet_lowpv.SetStats(0)

  h1_njet_highpv = TH1F('njet_highpv', 'njet_highpv', 9, jetbin)
  h1_njet_highpv.Sumw2()
  h1_njet_highpv.SetMinimum(0)
  h1_njet_highpv.GetXaxis().SetTitle('N_{jets}')
  h1_njet_highpv.GetYaxis().SetTitle('Efficiency')
  h1_njet_highpv.SetStats(0)

  h1_njet_lowMET = TH1F('njet_lowMET', 'njet_lowMET', 9, jetbin)
  h1_njet_lowMET.Sumw2()
  h1_njet_lowMET.SetMinimum(0)
  h1_njet_lowMET.GetXaxis().SetTitle('N_{jets}')
  h1_njet_lowMET.GetYaxis().SetTitle('Efficiency')
  h1_njet_lowMET.SetStats(0)

  h1_njet_highMET = TH1F('njet_highMET', 'njet_highMET', 9, jetbin)
  h1_njet_highMET.Sumw2()
  h1_njet_highMET.SetMinimum(0)
  h1_njet_highMET.GetXaxis().SetTitle('N_{jets}')
  h1_njet_highMET.GetYaxis().SetTitle('Efficiency')
  h1_njet_highMET.SetStats(0)

  h1_met = TH1F('met', 'met', 8, metbin)
  h1_met.Sumw2()
  h1_met.SetMinimum(0)
  h1_met.GetXaxis().SetTitle('MET [GeV]')
  h1_met.GetYaxis().SetTitle('Efficiency')
  h1_met.SetStats(0)

  h1_met_lowjet = TH1F('met_lowjet', 'met_lowjet', 8, metbin)
  h1_met_lowjet.Sumw2()
  h1_met_lowjet.SetMinimum(0)
  h1_met_lowjet.GetXaxis().SetTitle('MET [GeV]')
  h1_met_lowjet.GetYaxis().SetTitle('Efficiency')
  h1_met_lowjet.SetStats(0)

  h1_met_highjet = TH1F('met_highjet', 'met_highjet', 8, metbin)
  h1_met_highjet.Sumw2()
  h1_met_highjet.SetMinimum(0)
  h1_met_highjet.GetXaxis().SetTitle('MET [GeV]')
  h1_met_highjet.GetYaxis().SetTitle('Efficiency')
  h1_met_highjet.SetStats(0)

  h1_met_lowpv = TH1F('met_lowpv', 'met_lowpv', 8, metbin)
  h1_met_lowpv.Sumw2()
  h1_met_lowpv.SetMinimum(0)
  h1_met_lowpv.GetXaxis().SetTitle('MET [GeV]')
  h1_met_lowpv.GetYaxis().SetTitle('Efficiency')
  h1_met_lowpv.SetStats(0)

  h1_met_highpv = TH1F('met_highpv', 'met_highpv', 8, metbin)
  h1_met_highpv.Sumw2()
  h1_met_highpv.SetMinimum(0)
  h1_met_highpv.GetXaxis().SetTitle('MET [GeV]')
  h1_met_highpv.GetYaxis().SetTitle('Efficiency')
  h1_met_highpv.SetStats(0)

#  h1_nvtx = TH1F('nvtx', 'nvtx',30, 0, 60)
#  h1_nvtx.Sumw2()
#  h1_nvtx.SetMinimum(0)
#  h1_nvtx.SetStats(0)
  h1_pu = TH1F('pu', 'pu',40, 0, 80)
  h1_pu.Sumw2()
  h1_pu.SetMinimum(0)
  h1_pu.SetStats(0)

  h1_putrue = TH1F('putrue', 'putrue',40, 0, 80)
  h1_putrue.Sumw2()
  h1_putrue.SetMinimum(0)
  h1_putrue.SetStats(0)

  h2_l1pteta = TH2D('l1pteta', 'l1pteta', 6,tdl1ptbin,4,tdlepetabin)
  h2_l1pteta.Sumw2()
  h2_l1pteta.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_l1pteta.GetYaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_l1pteta.SetStats(0)

  h2_l1pteta_lowjet = TH2D('l1pteta_lowjet', 'l1pteta_lowjet', 6,tdl1ptbin,4,tdlepetabin)
  h2_l1pteta_lowjet.Sumw2()
  h2_l1pteta_lowjet.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_l1pteta_lowjet.GetYaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_l1pteta_lowjet.SetStats(0)

  h2_l1pteta_highjet = TH2D('l1pteta_highjet', 'l1pteta_highjet', 6,tdl1ptbin,4,tdlepetabin)
  h2_l1pteta_highjet.Sumw2()
  h2_l1pteta_highjet.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_l1pteta_highjet.GetYaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_l1pteta_highjet.SetStats(0)

  h2_l1pteta_lowpv = TH2D('l1pteta_lowpv', 'l1pteta_lowpv', 6,tdl1ptbin,4,tdlepetabin)
  h2_l1pteta_lowpv.Sumw2()
  h2_l1pteta_lowpv.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_l1pteta_lowpv.GetYaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_l1pteta_lowpv.SetStats(0)

  h2_l1pteta_highpv = TH2D('l1pteta_highpv', 'l1pteta_highpv', 6,tdl1ptbin,4,tdlepetabin)
  h2_l1pteta_highpv.Sumw2()
  h2_l1pteta_highpv.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_l1pteta_highpv.GetYaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_l1pteta_highpv.SetStats(0)

  h2_l1pteta_lowMET = TH2D('l1pteta_lowMET', 'l1pteta_lowMET', 6,tdl1ptbin,4,tdlepetabin)
  h2_l1pteta_lowMET.Sumw2()
  h2_l1pteta_lowMET.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_l1pteta_lowMET.GetYaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_l1pteta_lowMET.SetStats(0)

  h2_l1pteta_highMET = TH2D('l1pteta_highMET', 'l1pteta_highMET', 6,tdl1ptbin,4,tdlepetabin)
  h2_l1pteta_highMET.Sumw2()
  h2_l1pteta_highMET.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_l1pteta_highMET.GetYaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_l1pteta_highMET.SetStats(0)

  h2_l2pteta = TH2D('l2pteta', 'l2pteta', 6,tdl1ptbin,4,tdlepetabin)
  h2_l2pteta.Sumw2()
  h2_l2pteta.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_l2pteta.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_l2pteta.SetStats(0)

  h2_l2pteta_lowjet = TH2D('l2pteta_lowjet', 'l2pteta_lowjet', 6,tdl1ptbin,4,tdlepetabin)
  h2_l2pteta_lowjet.Sumw2()
  h2_l2pteta_lowjet.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_l2pteta_lowjet.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_l2pteta_lowjet.SetStats(0)

  h2_l2pteta_highjet = TH2D('l2pteta_highjet', 'l2pteta_highjet', 6,tdl1ptbin,4,tdlepetabin)
  h2_l2pteta_highjet.Sumw2()
  h2_l2pteta_highjet.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_l2pteta_highjet.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_l2pteta_highjet.SetStats(0)

  h2_l2pteta_lowpv = TH2D('l2pteta_lowpv', 'l2pteta_lowpv', 6,tdl1ptbin,4,tdlepetabin)
  h2_l2pteta_lowpv.Sumw2()
  h2_l2pteta_lowpv.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_l2pteta_lowpv.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_l2pteta_lowpv.SetStats(0)

  h2_l2pteta_highpv = TH2D('l2pteta_highpv', 'l2pteta_highpv', 6,tdl1ptbin,4,tdlepetabin)
  h2_l2pteta_highpv.Sumw2()
  h2_l2pteta_highpv.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_l2pteta_highpv.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_l2pteta_highpv.SetStats(0)

  h2_l2pteta_lowMET = TH2D('l2pteta_lowMET', 'l2pteta_lowMET', 6,tdl1ptbin,4,tdlepetabin)
  h2_l2pteta_lowMET.Sumw2()
  h2_l2pteta_lowMET.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_l2pteta_lowMET.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_l2pteta_lowMET.SetStats(0)

  h2_l2pteta_highMET = TH2D('l2pteta_highMET', 'l2pteta_highMET', 6,tdl1ptbin,4,tdlepetabin)
  h2_l2pteta_highMET.Sumw2()
  h2_l2pteta_highMET.GetXaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_l2pteta_highMET.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_l2pteta_highMET.SetStats(0)

  h2_l1l2pt = TH2D('l1l2pt', 'l1l2pt', 6, tdl1ptbin, 6, tdl2ptbin)
  h2_l1l2pt.Sumw2()
  h2_l1l2pt.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_l1l2pt.GetYaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_l1l2pt.SetStats(0)

  h2_l1l2pt_lowjet = TH2D('l1l2pt_lowjet', 'l1l2pt_lowjet', 6, tdl1ptbin, 6, tdl2ptbin)
  h2_l1l2pt_lowjet.Sumw2()
  h2_l1l2pt_lowjet.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_l1l2pt_lowjet.GetYaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_l1l2pt_lowjet.SetStats(0)

  h2_l1l2pt_highjet = TH2D('l1l2pt_highjet', 'l1l2pt_highjet', 6, tdl1ptbin, 6, tdl2ptbin)
  h2_l1l2pt_highjet.Sumw2()
  h2_l1l2pt_highjet.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_l1l2pt_highjet.GetYaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_l1l2pt_highjet.SetStats(0)

  h2_l1l2pt_lowpv = TH2D('l1l2pt_lowpv', 'l1l2pt_lowpv', 6, tdl1ptbin, 6, tdl2ptbin)
  h2_l1l2pt_lowpv.Sumw2()
  h2_l1l2pt_lowpv.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_l1l2pt_lowpv.GetYaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_l1l2pt_lowpv.SetStats(0)

  h2_l1l2pt_highpv = TH2D('l1l2pt_highpv', 'l1l2pt_highpv', 6, tdl1ptbin, 6, tdl2ptbin)
  h2_l1l2pt_highpv.Sumw2()
  h2_l1l2pt_highpv.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_l1l2pt_highpv.GetYaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_l1l2pt_highpv.SetStats(0)

  h2_l1l2pt_lowMET = TH2D('l1l2pt_lowMET', 'l1l2pt_lowMET', 6, tdl1ptbin, 6, tdl2ptbin)
  h2_l1l2pt_lowMET.Sumw2()
  h2_l1l2pt_lowMET.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_l1l2pt_lowMET.GetYaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_l1l2pt_lowMET.SetStats(0)

  h2_l1l2pt_highMET = TH2D('l1l2pt_highMET', 'l1l2pt_highMET', 6, tdl1ptbin, 6, tdl2ptbin)
  h2_l1l2pt_highMET.Sumw2()
  h2_l1l2pt_highMET.GetXaxis().SetTitle('Leading Lepton P_{T} [GeV]')
  h2_l1l2pt_highMET.GetYaxis().SetTitle('Subleading Lepton P_{T} [GeV]')
  h2_l1l2pt_highMET.SetStats(0)

  h2_l1l2eta = TH2D('l1l2eta','l1l2eta',4,tdlepetabin,4,tdlepetabin)
  h2_l1l2eta.Sumw2()
  h2_l1l2eta.GetXaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_l1l2eta.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_l1l2eta.SetStats(0)
  
  h2_l1l2eta_lowjet = TH2D('l1l2eta_lowjet','l1l2eta_lowjet',4,tdlepetabin,4,tdlepetabin)
  h2_l1l2eta_lowjet.Sumw2()
  h2_l1l2eta_lowjet.GetXaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_l1l2eta_lowjet.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_l1l2eta_lowjet.SetStats(0)
  
  h2_l1l2eta_highjet = TH2D('l1l2eta_highjet','l1l2eta_highjet',4,tdlepetabin,4,tdlepetabin)
  h2_l1l2eta_highjet.Sumw2()
  h2_l1l2eta_highjet.GetXaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_l1l2eta_highjet.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_l1l2eta_highjet.SetStats(0)
  
  h2_l1l2eta_lowpv = TH2D('l1l2eta_lowpv','l1l2eta_lowpv',4,tdlepetabin,4,tdlepetabin)
  h2_l1l2eta_lowpv.Sumw2()
  h2_l1l2eta_lowpv.GetXaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_l1l2eta_lowpv.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_l1l2eta_lowpv.SetStats(0)
  
  h2_l1l2eta_highpv = TH2D('l1l2eta_highpv','l1l2eta_highpv',4,tdlepetabin,4,tdlepetabin)
  h2_l1l2eta_highpv.Sumw2()
  h2_l1l2eta_highpv.GetXaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_l1l2eta_highpv.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_l1l2eta_highpv.SetStats(0)
  
  h2_l1l2eta_lowMET = TH2D('l1l2eta_lowMET','l1l2eta_lowMET',4,tdlepetabin,4,tdlepetabin)
  h2_l1l2eta_lowMET.Sumw2()
  h2_l1l2eta_lowMET.GetXaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_l1l2eta_lowMET.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_l1l2eta_lowMET.SetStats(0)
  
  h2_l1l2eta_highMET = TH2D('l1l2eta_highMET','l1l2eta_highMET',4,tdlepetabin,4,tdlepetabin)
  h2_l1l2eta_highMET.Sumw2()
  h2_l1l2eta_highMET.GetXaxis().SetTitle('Leading Lepton #||{#eta}')
  h2_l1l2eta_highMET.GetYaxis().SetTitle('Subleading Lepton #||{#eta}')
  h2_l1l2eta_highMET.SetStats(0)
  
  l1p4=TLorentzVector()
  l2p4=TLorentzVector()

  all_events1 = TH1F('all_events1','lep_tag',1,0,1)
  all_events2 = TH1F('all_events2','met_tag',1,0,1)
  all_events3 = TH1F('all_events3','lepmet_tag',1,0,1)
  pass_lep_trigger= TH1F('pass_lep_trigger','pass_lep_trigger',1,0,1)
  pass_met_trigger= TH1F('pass_met_trigger','pass_met_trigger',1,0,1)
  pass_lepmet_trigger= TH1F('pass_lepmet_trigger','pass_lepmet_trigger',1,0,1)

  for ientry in range(0,entries):
    treein.GetEntry(ientry)
    if 'TT' in filename:
      met=treein.MET_T1Smear_pt
    else:
      met=treein.MET_T1_pt

    if ientry%10000==0:print 'processing ',ientry
    if not (treein.Flag_goodVertices and treein.Flag_globalSuperTightHalo2016Filter and treein.Flag_HBHENoiseFilter and treein.Flag_HBHENoiseIsoFilter and treein.Flag_EcalDeadCellTriggerPrimitiveFilter and treein.Flag_BadPFMuonFilter and treein.Flag_eeBadScFilter and treein.Flag_ecalBadCalibFilter): continue

    if (channel==22):
      if not (treein.DY_region==3 or treein.ttc_region==3): continue
      if treein.DY_region==3:
	l1p4.SetPtEtaPhiM(treein.DY_l1_pt, treein.DY_l1_eta,treein.DY_l1_phi,treein.DY_l1_mass)
	l2p4.SetPtEtaPhiM(treein.DY_l2_pt, treein.DY_l2_eta,treein.DY_l2_phi,treein.DY_l2_mass)
	if 'TT' in filename:
	  weight=treein.Electron_RECO_SF[treein.DY_l1_id]*treein.Electron_RECO_SF[treein.DY_l2_id]*treein.Electron_CutBased_TightID_SF[treein.DY_l1_id]*treein.Electron_CutBased_TightID_SF[treein.DY_l2_id]*treein.puWeight*treein.PrefireWeight
	else:
	  weight=1.
      if treein.ttc_region==3:
	l1p4.SetPtEtaPhiM(treein.ttc_l1_pt, treein.ttc_l1_eta,treein.ttc_l1_phi,treein.ttc_l1_mass)
        l2p4.SetPtEtaPhiM(treein.ttc_l2_pt, treein.ttc_l2_eta,treein.ttc_l2_phi,treein.ttc_l2_mass)
	if 'TT' in filename:
	  weight=treein.Electron_RECO_SF[treein.ttc_l1_id]*treein.Electron_RECO_SF[treein.ttc_l2_id]*treein.Electron_CutBased_TightID_SF[treein.ttc_l1_id]*treein.Electron_CutBased_TightID_SF[treein.ttc_l2_id]*treein.puWeight*treein.PrefireWeight
	else:
	  weight=1.

      if (l1p4+l2p4).M()<20:continue
      if not (l1p4.Pt()>30 or l2p4.Pt()>30):continue
      if (l1p4.DeltaR(l2p4)<0.3): continue
      if met<100:continue

#      if not ((l1p4+l2p4).M()<76 or (l1p4+l2p4).M()>106): continue

      all_events1.Fill(0.5,weight)
      all_events2.Fill(0.5,weight)
      all_events3.Fill(0.5,weight)
      if (treein.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL or treein.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ or treein.HLT_passEle32WPTight or treein.HLT_Ele35_WPTight_Gsf):
	pass_lep_trigger.Fill(0.5,weight)
      if (treein.HLT_PFMET120_PFMHT120_IDTight or treein.HLT_PFMETNoMu120_PFMHTNoMu120_IDTight or treein.HLT_PFHT500_PFMET100_PFMHT100_IDTight or treein.HLT_PFHT700_PFMET85_PFMHT85_IDTight or treein.HLT_PFHT800_PFMET75_PFMHT75_IDTight):
	pass_met_trigger.Fill(0.5,weight)
        h1_pre_l1pt.Fill(l1p4.Pt(),weight)
        h1_pre_l1eta.Fill(l1p4.Eta(),weight)
        h1_pre_l2pt.Fill(l2p4.Pt(),weight)
        h1_pre_l2eta.Fill(l2p4.Eta(),weight)
        h1_pre_njet.Fill(treein.n_tight_jet,weight)
        h1_pre_met.Fill(met,weight)
        h2_pre_l1pteta.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
        h2_pre_l2pteta.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
        h2_pre_l1l2pt.Fill(l1p4.Pt(),l2p4.Pt(),weight)
        h2_pre_l1l2eta.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	if treein.n_tight_jet>3:
	  h1_pre_l1pt_highjet.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_highjet.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_highjet.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_highjet.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_highjet.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_highjet.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_highjet.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_highjet.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	else:
	  h1_pre_l1pt_lowjet.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_lowjet.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_lowjet.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_lowjet.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_lowjet.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_lowjet.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_lowjet.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_lowjet.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	if (treein.PV_npvs)>30:
	  h1_pre_l1pt_highpv.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_highpv.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_highpv.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_highpv.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_highpv.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_highpv.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_highpv.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_highpv.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	else:
	  h1_pre_l1pt_lowpv.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_lowpv.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_lowpv.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_lowpv.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_lowpv.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_lowpv.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_lowpv.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_lowpv.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	if met>150:
	  h1_pre_l1pt_highMET.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_highMET.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_highMET.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_highMET.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_highMET.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_highMET.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_highMET.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_highMET.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	else:
	  h1_pre_l1pt_lowMET.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_lowMET.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_lowMET.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_lowMET.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_lowMET.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_lowMET.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_lowMET.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_lowMET.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)

        if (treein.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL or treein.HLT_Ele23_Ele12_CaloIdL_TrackIdL_IsoVL_DZ or treein.HLT_passEle32WPTight or treein.HLT_Ele35_WPTight_Gsf):
	  pass_lepmet_trigger.Fill(0.5,weight)
          h1_l1pt.Fill(l1p4.Pt(),weight)
          h1_l1eta.Fill(l1p4.Eta(),weight)
          h1_l2pt.Fill(l2p4.Pt(),weight)
          h1_l2eta.Fill(l2p4.Eta(),weight)
          h1_njet.Fill(treein.n_tight_jet,weight)
          h1_met.Fill(met,weight)
          h2_l1pteta.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_l2pteta.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_l1l2pt.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_l1l2eta.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  if treein.n_tight_jet>3:
	    h1_l1pt_highjet.Fill(l1p4.Pt(),weight)
	    h1_l1eta_highjet.Fill(l1p4.Eta(),weight)
            h1_l2pt_highjet.Fill(l2p4.Pt(),weight)
            h1_l2eta_highjet.Fill(l2p4.Eta(),weight)
            h2_l1pteta_highjet.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_highjet.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_highjet.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_highjet.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  else:
	    h1_l1pt_lowjet.Fill(l1p4.Pt(),weight)
	    h1_l1eta_lowjet.Fill(l1p4.Eta(),weight)
            h1_l2pt_lowjet.Fill(l2p4.Pt(),weight)
            h1_l2eta_lowjet.Fill(l2p4.Eta(),weight)
            h2_l1pteta_lowjet.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_lowjet.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_lowjet.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_lowjet.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  if (treein.PV_npvs)>30:
	    h1_l1pt_highpv.Fill(l1p4.Pt(),weight)
	    h1_l1eta_highpv.Fill(l1p4.Eta(),weight)
            h1_l2pt_highpv.Fill(l2p4.Pt(),weight)
            h1_l2eta_highpv.Fill(l2p4.Eta(),weight)
            h2_l1pteta_highpv.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_highpv.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_highpv.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_highpv.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  else:
	    h1_l1pt_lowpv.Fill(l1p4.Pt(),weight)
	    h1_l1eta_lowpv.Fill(l1p4.Eta(),weight)
            h1_l2pt_lowpv.Fill(l2p4.Pt(),weight)
            h1_l2eta_lowpv.Fill(l2p4.Eta(),weight)
            h2_l1pteta_lowpv.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_lowpv.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_lowpv.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_lowpv.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  if met>150:
	    h1_l1pt_highMET.Fill(l1p4.Pt(),weight)
	    h1_l1eta_highMET.Fill(l1p4.Eta(),weight)
            h1_l2pt_highMET.Fill(l2p4.Pt(),weight)
            h1_l2eta_highMET.Fill(l2p4.Eta(),weight)
            h2_l1pteta_highMET.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_highMET.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_highMET.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_highMET.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  else:
	    h1_l1pt_lowMET.Fill(l1p4.Pt(),weight)
	    h1_l1eta_lowMET.Fill(l1p4.Eta(),weight)
            h1_l2pt_lowMET.Fill(l2p4.Pt(),weight)
            h1_l2eta_lowMET.Fill(l2p4.Eta(),weight)
            h2_l1pteta_lowMET.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_lowMET.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_lowMET.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_lowMET.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  
    if (channel==26):
      if not (treein.DY_region==1 or treein.ttc_region==1): continue
      if treein.DY_region==1:
	l1p4.SetPtEtaPhiM(treein.DY_l1_pt, treein.DY_l1_eta,treein.DY_l1_phi,treein.DY_l1_mass)
	l2p4.SetPtEtaPhiM(treein.DY_l2_pt, treein.DY_l2_eta,treein.DY_l2_phi,treein.DY_l2_mass)
	if 'TT' in filename:
	  weight=treein.Muon_CutBased_TightID_SF[treein.DY_l1_id]*treein.Muon_CutBased_TightID_SF[treein.DY_l2_id]*treein.Muon_TightRelIso_TightIDandIPCut_SF[treein.DY_l1_id]*treein.Muon_TightRelIso_TightIDandIPCut_SF[treein.DY_l2_id]*treein.puWeight*treein.PrefireWeight
	else:
	  weight=1.
      if treein.ttc_region==1:
	l1p4.SetPtEtaPhiM(treein.ttc_l1_pt, treein.ttc_l1_eta,treein.ttc_l1_phi,treein.ttc_l1_mass)
        l2p4.SetPtEtaPhiM(treein.ttc_l2_pt, treein.ttc_l2_eta,treein.ttc_l2_phi,treein.ttc_l2_mass)
	if 'TT' in filename:
	  weight=treein.Muon_CutBased_TightID_SF[treein.ttc_l1_id]*treein.Muon_CutBased_TightID_SF[treein.ttc_l2_id]*treein.Muon_TightRelIso_TightIDandIPCut_SF[treein.ttc_l1_id]*treein.Muon_TightRelIso_TightIDandIPCut_SF[treein.ttc_l2_id]*treein.puWeight*treein.PrefireWeight
	else:
	  weight=1.

      if (l1p4+l2p4).M()<20:continue
      if not (l1p4.Pt()>30 or l2p4.Pt()>30):continue
      if (l1p4.DeltaR(l2p4)<0.3): continue
      if met<100:continue

#      if not ((l1p4+l2p4).M()<76 or (l1p4+l2p4).M()>106): continue

      all_events1.Fill(0.5,weight)
      all_events2.Fill(0.5,weight)
      all_events3.Fill(0.5,weight)
      if (treein.HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8 or treein.HLT_IsoMu27):
	pass_lep_trigger.Fill(0.5,weight)
      if (treein.HLT_PFMET120_PFMHT120_IDTight or treein.HLT_PFMETNoMu120_PFMHTNoMu120_IDTight or treein.HLT_PFHT500_PFMET100_PFMHT100_IDTight or treein.HLT_PFHT700_PFMET85_PFMHT85_IDTight or treein.HLT_PFHT800_PFMET75_PFMHT75_IDTight):
	pass_met_trigger.Fill(0.5,weight)
        h1_pre_l1pt.Fill(l1p4.Pt(),weight)
        h1_pre_l1eta.Fill(l1p4.Eta(),weight)
        h1_pre_l2pt.Fill(l2p4.Pt(),weight)
        h1_pre_l2eta.Fill(l2p4.Eta(),weight)
        h1_pre_njet.Fill(treein.n_tight_jet,weight)
        h1_pre_met.Fill(met,weight)
        h2_pre_l1pteta.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
        h2_pre_l2pteta.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
        h2_pre_l1l2pt.Fill(l1p4.Pt(),l2p4.Pt(),weight)
        h2_pre_l1l2eta.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	if treein.n_tight_jet>3:
	  h1_pre_l1pt_highjet.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_highjet.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_highjet.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_highjet.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_highjet.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_highjet.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_highjet.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_highjet.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	else:
	  h1_pre_l1pt_lowjet.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_lowjet.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_lowjet.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_lowjet.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_lowjet.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_lowjet.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_lowjet.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_lowjet.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	if (treein.PV_npvs)>30:
	  h1_pre_l1pt_highpv.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_highpv.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_highpv.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_highpv.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_highpv.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_highpv.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_highpv.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_highpv.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	else:
	  h1_pre_l1pt_lowpv.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_lowpv.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_lowpv.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_lowpv.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_lowpv.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_lowpv.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_lowpv.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_lowpv.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	if met>150:
	  h1_pre_l1pt_highMET.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_highMET.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_highMET.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_highMET.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_highMET.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_highMET.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_highMET.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_highMET.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	else:
	  h1_pre_l1pt_lowMET.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_lowMET.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_lowMET.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_lowMET.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_lowMET.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_lowMET.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_lowMET.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_lowMET.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)

        if (treein.HLT_Mu17_TrkIsoVVL_Mu8_TrkIsoVVL_DZ_Mass8 or treein.HLT_IsoMu27):
	  pass_lepmet_trigger.Fill(0.5,weight)
          h1_l1pt.Fill(l1p4.Pt(),weight)
          h1_l1eta.Fill(l1p4.Eta(),weight)
          h1_l2pt.Fill(l2p4.Pt(),weight)
          h1_l2eta.Fill(l2p4.Eta(),weight)
          h1_njet.Fill(treein.n_tight_jet,weight)
          h1_met.Fill(met,weight)
          h2_l1pteta.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_l2pteta.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_l1l2pt.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_l1l2eta.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  if treein.n_tight_jet>3:
	    h1_l1pt_highjet.Fill(l1p4.Pt(),weight)
	    h1_l1eta_highjet.Fill(l1p4.Eta(),weight)
            h1_l2pt_highjet.Fill(l2p4.Pt(),weight)
            h1_l2eta_highjet.Fill(l2p4.Eta(),weight)
            h2_l1pteta_highjet.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_highjet.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_highjet.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_highjet.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  else:
	    h1_l1pt_lowjet.Fill(l1p4.Pt(),weight)
	    h1_l1eta_lowjet.Fill(l1p4.Eta(),weight)
            h1_l2pt_lowjet.Fill(l2p4.Pt(),weight)
            h1_l2eta_lowjet.Fill(l2p4.Eta(),weight)
            h2_l1pteta_lowjet.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_lowjet.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_lowjet.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_lowjet.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  if (treein.PV_npvs)>30:
	    h1_l1pt_highpv.Fill(l1p4.Pt(),weight)
	    h1_l1eta_highpv.Fill(l1p4.Eta(),weight)
            h1_l2pt_highpv.Fill(l2p4.Pt(),weight)
            h1_l2eta_highpv.Fill(l2p4.Eta(),weight)
            h2_l1pteta_highpv.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_highpv.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_highpv.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_highpv.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  else:
	    h1_l1pt_lowpv.Fill(l1p4.Pt(),weight)
	    h1_l1eta_lowpv.Fill(l1p4.Eta(),weight)
            h1_l2pt_lowpv.Fill(l2p4.Pt(),weight)
            h1_l2eta_lowpv.Fill(l2p4.Eta(),weight)
            h2_l1pteta_lowpv.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_lowpv.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_lowpv.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_lowpv.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  if met>150:
	    h1_l1pt_highMET.Fill(l1p4.Pt(),weight)
	    h1_l1eta_highMET.Fill(l1p4.Eta(),weight)
            h1_l2pt_highMET.Fill(l2p4.Pt(),weight)
            h1_l2eta_highMET.Fill(l2p4.Eta(),weight)
            h2_l1pteta_highMET.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_highMET.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_highMET.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_highMET.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  else:
	    h1_l1pt_lowMET.Fill(l1p4.Pt(),weight)
	    h1_l1eta_lowMET.Fill(l1p4.Eta(),weight)
            h1_l2pt_lowMET.Fill(l2p4.Pt(),weight)
            h1_l2eta_lowMET.Fill(l2p4.Eta(),weight)
            h2_l1pteta_lowMET.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_lowMET.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_lowMET.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_lowMET.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)

    if (channel==24):
      if not (treein.DY_region==2 or treein.ttc_region==2): continue
      if treein.DY_region==2:
	l1p4.SetPtEtaPhiM(treein.Muon_corrected_pt[treein.DY_l1_id], treein.Muon_eta[treein.DY_l1_id],treein.Muon_phi[treein.DY_l1_id],treein.Muon_mass[treein.DY_l1_id])
	l2p4.SetPtEtaPhiM(treein.Electron_pt[treein.DY_l2_id], treein.Electron_eta[treein.DY_l2_id],treein.Electron_phi[treein.DY_l2_id],treein.Electron_mass[treein.DY_l2_id])
	if 'TT' in filename:
	  weight=treein.Muon_CutBased_TightID_SF[treein.DY_l1_id]*treein.Muon_TightRelIso_TightIDandIPCut_SF[treein.DY_l1_id]*treein.Electron_RECO_SF[treein.DY_l2_id]*treein.Electron_CutBased_TightID_SF[treein.DY_l2_id]*treein.puWeight*treein.PrefireWeight
	else:
	  weight=1.
      if treein.ttc_region==2:
	l1p4.SetPtEtaPhiM(treein.ttc_l1_pt, treein.ttc_l1_eta,treein.ttc_l1_phi,treein.ttc_l1_mass)
        l2p4.SetPtEtaPhiM(treein.ttc_l2_pt, treein.ttc_l2_eta,treein.ttc_l2_phi,treein.ttc_l2_mass)
	if 'TT' in filename:
	  weight=treein.Muon_CutBased_TightID_SF[treein.ttc_l1_id]*treein.Muon_TightRelIso_TightIDandIPCut_SF[treein.ttc_l1_id]*treein.Electron_RECO_SF[treein.ttc_l2_id]*treein.Electron_CutBased_TightID_SF[treein.ttc_l2_id]*treein.puWeight*treein.PrefireWeight
	else:
	  weight=1.

      if (l1p4+l2p4).M()<20:continue
      if not (l1p4.Pt()>30 or l2p4.Pt()>30):continue
      if (l1p4.DeltaR(l2p4)<0.3): continue
      if met<100:continue

#      if not ((l1p4+l2p4).M()<76 or (l1p4+l2p4).M()>106): continue

      all_events1.Fill(0.5,weight)
      all_events2.Fill(0.5,weight)
      all_events3.Fill(0.5,weight)
      if (treein.HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ or treein.HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ or treein.HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ or treein.HLT_IsoMu27 or treein.HLT_passEle32WPTight or treein.HLT_Ele35_WPTight_Gsf):
	pass_lep_trigger.Fill(0.5,weight)
      if (treein.HLT_PFMET120_PFMHT120_IDTight or treein.HLT_PFMETNoMu120_PFMHTNoMu120_IDTight or treein.HLT_PFHT500_PFMET100_PFMHT100_IDTight or treein.HLT_PFHT700_PFMET85_PFMHT85_IDTight or treein.HLT_PFHT800_PFMET75_PFMHT75_IDTight):
	pass_met_trigger.Fill(0.5,weight)
        h1_pre_l1pt.Fill(l1p4.Pt(),weight)
        h1_pre_l1eta.Fill(l1p4.Eta(),weight)
        h1_pre_l2pt.Fill(l2p4.Pt(),weight)
        h1_pre_l2eta.Fill(l2p4.Eta(),weight)
        h1_pre_njet.Fill(treein.n_tight_jet,weight)
        h1_pre_met.Fill(met,weight)
        h2_pre_l1pteta.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
        h2_pre_l2pteta.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
        h2_pre_l1l2pt.Fill(l1p4.Pt(),l2p4.Pt(),weight)
        h2_pre_l1l2eta.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	if treein.n_tight_jet>3:
	  h1_pre_l1pt_highjet.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_highjet.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_highjet.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_highjet.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_highjet.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_highjet.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_highjet.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_highjet.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	else:
	  h1_pre_l1pt_lowjet.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_lowjet.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_lowjet.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_lowjet.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_lowjet.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_lowjet.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_lowjet.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_lowjet.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	if (treein.PV_npvs)>30:
	  h1_pre_l1pt_highpv.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_highpv.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_highpv.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_highpv.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_highpv.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_highpv.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_highpv.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_highpv.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	else:
	  h1_pre_l1pt_lowpv.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_lowpv.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_lowpv.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_lowpv.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_lowpv.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_lowpv.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_lowpv.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_lowpv.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	if met>150:
	  h1_pre_l1pt_highMET.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_highMET.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_highMET.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_highMET.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_highMET.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_highMET.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_highMET.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_highMET.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	else:
	  h1_pre_l1pt_lowMET.Fill(l1p4.Pt(),weight)
	  h1_pre_l1eta_lowMET.Fill(l1p4.Eta(),weight)
          h1_pre_l2pt_lowMET.Fill(l2p4.Pt(),weight)
          h1_pre_l2eta_lowMET.Fill(l2p4.Eta(),weight)
          h2_pre_l1pteta_lowMET.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_pre_l2pteta_lowMET.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_pre_l1l2pt_lowMET.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_pre_l1l2eta_lowMET.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)

        if (treein.HLT_Mu8_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ or treein.HLT_Mu12_TrkIsoVVL_Ele23_CaloIdL_TrackIdL_IsoVL_DZ or treein.HLT_Mu23_TrkIsoVVL_Ele12_CaloIdL_TrackIdL_IsoVL_DZ or treein.HLT_IsoMu27 or treein.HLT_passEle32WPTight or treein.HLT_Ele35_WPTight_Gsf):
	  pass_lepmet_trigger.Fill(0.5,weight)
          h1_l1pt.Fill(l1p4.Pt(),weight)
          h1_l1eta.Fill(l1p4.Eta(),weight)
          h1_l2pt.Fill(l2p4.Pt(),weight)
          h1_l2eta.Fill(l2p4.Eta(),weight)
          h1_njet.Fill(treein.n_tight_jet,weight)
          h1_met.Fill(met,weight)
          h2_l1pteta.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
          h2_l2pteta.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
          h2_l1l2pt.Fill(l1p4.Pt(),l2p4.Pt(),weight)
          h2_l1l2eta.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  if treein.n_tight_jet>3:
	    h1_l1pt_highjet.Fill(l1p4.Pt(),weight)
	    h1_l1eta_highjet.Fill(l1p4.Eta(),weight)
            h1_l2pt_highjet.Fill(l2p4.Pt(),weight)
            h1_l2eta_highjet.Fill(l2p4.Eta(),weight)
            h2_l1pteta_highjet.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_highjet.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_highjet.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_highjet.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  else:
	    h1_l1pt_lowjet.Fill(l1p4.Pt(),weight)
	    h1_l1eta_lowjet.Fill(l1p4.Eta(),weight)
            h1_l2pt_lowjet.Fill(l2p4.Pt(),weight)
            h1_l2eta_lowjet.Fill(l2p4.Eta(),weight)
            h2_l1pteta_lowjet.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_lowjet.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_lowjet.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_lowjet.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  if (treein.PV_npvs)>30:
	    h1_l1pt_highpv.Fill(l1p4.Pt(),weight)
	    h1_l1eta_highpv.Fill(l1p4.Eta(),weight)
            h1_l2pt_highpv.Fill(l2p4.Pt(),weight)
            h1_l2eta_highpv.Fill(l2p4.Eta(),weight)
            h2_l1pteta_highpv.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_highpv.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_highpv.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_highpv.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  else:
	    h1_l1pt_lowpv.Fill(l1p4.Pt(),weight)
	    h1_l1eta_lowpv.Fill(l1p4.Eta(),weight)
            h1_l2pt_lowpv.Fill(l2p4.Pt(),weight)
            h1_l2eta_lowpv.Fill(l2p4.Eta(),weight)
            h2_l1pteta_lowpv.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_lowpv.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_lowpv.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_lowpv.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  if met>150:
	    h1_l1pt_highMET.Fill(l1p4.Pt(),weight)
	    h1_l1eta_highMET.Fill(l1p4.Eta(),weight)
            h1_l2pt_highMET.Fill(l2p4.Pt(),weight)
            h1_l2eta_highMET.Fill(l2p4.Eta(),weight)
            h2_l1pteta_highMET.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_highMET.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_highMET.Fill(l1p4.Pt(),l2p4.Pt(),weight)
            h2_l1l2eta_highMET.Fill(abs(l1p4.Eta()),abs(l2p4.Eta()),weight)
	  else:
	    h1_l1pt_lowMET.Fill(l1p4.Pt(),weight)
	    h1_l1eta_lowMET.Fill(l1p4.Eta(),weight)
            h1_l2pt_lowMET.Fill(l2p4.Pt(),weight)
            h1_l2eta_lowMET.Fill(l2p4.Eta(),weight)
            h2_l1pteta_lowMET.Fill(l1p4.Pt(),abs(l1p4.Eta()),weight)
            h2_l2pteta_lowMET.Fill(l2p4.Pt(),abs(l2p4.Eta()),weight)
            h2_l1l2pt_lowMET.Fill(l1p4.Pt(),l2p4.Pt(),weight)
  
  Eff_l1pt=TEfficiency(h1_l1pt, h1_pre_l1pt)
  Eff_l1pt.SetTitle('Eff l1pt')
  Eff_l1pt_lowjet=TEfficiency(h1_l1pt_lowjet, h1_pre_l1pt_lowjet)
  Eff_l1pt_lowjet.SetTitle('Eff l1pt_lowjet')
  Eff_l1pt_highjet=TEfficiency(h1_l1pt_highjet, h1_pre_l1pt_highjet)
  Eff_l1pt_highjet.SetTitle('Eff l1pt_highjet')
  Eff_l1pt_lowpv=TEfficiency(h1_l1pt_lowpv, h1_pre_l1pt_lowpv)
  Eff_l1pt_lowpv.SetTitle('Eff l1pt_lowpv')
  Eff_l1pt_highpv=TEfficiency(h1_l1pt_highpv, h1_pre_l1pt_highpv)
  Eff_l1pt_highpv.SetTitle('Eff l1pt_highpv')
  Eff_l1pt_lowMET=TEfficiency(h1_l1pt_lowMET, h1_pre_l1pt_lowMET)
  Eff_l1pt_lowMET.SetTitle('Eff l1pt_lowMET')
  Eff_l1pt_highMET=TEfficiency(h1_l1pt_highMET, h1_pre_l1pt_highMET)
  Eff_l1pt_highMET.SetTitle('Eff l1pt_highMET')

  Eff_l1eta=TEfficiency(h1_l1eta, h1_pre_l1eta)
  Eff_l1eta.SetTitle('Eff l1eta')
  Eff_l1eta_lowjet=TEfficiency(h1_l1eta_lowjet, h1_pre_l1eta_lowjet)
  Eff_l1eta_lowjet.SetTitle('Eff l1eta_lowjet')
  Eff_l1eta_highjet=TEfficiency(h1_l1eta_highjet, h1_pre_l1eta_highjet)
  Eff_l1eta_highjet.SetTitle('Eff l1eta_highjet')
  Eff_l1eta_lowpv=TEfficiency(h1_l1eta_lowpv, h1_pre_l1eta_lowpv)
  Eff_l1eta_lowpv.SetTitle('Eff l1eta_lowpv')
  Eff_l1eta_highpv=TEfficiency(h1_l1eta_highpv, h1_pre_l1eta_highpv)
  Eff_l1eta_highpv.SetTitle('Eff l1eta_highpv')
  Eff_l1eta_lowMET=TEfficiency(h1_l1eta_lowMET, h1_pre_l1eta_lowMET)
  Eff_l1eta_lowMET.SetTitle('Eff l1eta_lowMET')
  Eff_l1eta_highMET=TEfficiency(h1_l1eta_highMET, h1_pre_l1eta_highMET)
  Eff_l1eta_highMET.SetTitle('Eff l1eta_highMET')

  Eff_l2pt=TEfficiency(h1_l2pt, h1_pre_l2pt)
  Eff_l2pt.SetTitle('Eff l2pt')
  Eff_l2pt_lowjet=TEfficiency(h1_l2pt_lowjet, h1_pre_l2pt_lowjet)
  Eff_l2pt_lowjet.SetTitle('Eff l2pt_lowjet')
  Eff_l2pt_highjet=TEfficiency(h1_l2pt_highjet, h1_pre_l2pt_highjet)
  Eff_l2pt_highjet.SetTitle('Eff l2pt_highjet')
  Eff_l2pt_lowpv=TEfficiency(h1_l2pt_lowpv, h1_pre_l2pt_lowpv)
  Eff_l2pt_lowpv.SetTitle('Eff l2pt_lowpv')
  Eff_l2pt_highpv=TEfficiency(h1_l2pt_highpv, h1_pre_l2pt_highpv)
  Eff_l2pt_highpv.SetTitle('Eff l2pt_highpv')
  Eff_l2pt_lowMET=TEfficiency(h1_l2pt_lowMET, h1_pre_l2pt_lowMET)
  Eff_l2pt_lowMET.SetTitle('Eff l2pt_lowMET')
  Eff_l2pt_highMET=TEfficiency(h1_l2pt_highMET, h1_pre_l2pt_highMET)
  Eff_l2pt_highMET.SetTitle('Eff l2pt_highMET')

  Eff_l2eta=TEfficiency(h1_l2eta, h1_pre_l2eta)
  Eff_l2eta.SetTitle('Eff l2eta')
  Eff_l2eta_lowjet=TEfficiency(h1_l2eta_lowjet, h1_pre_l2eta_lowjet)
  Eff_l2eta_lowjet.SetTitle('Eff l2eta_lowjet')
  Eff_l2eta_highjet=TEfficiency(h1_l2eta_highjet, h1_pre_l2eta_highjet)
  Eff_l2eta_highjet.SetTitle('Eff l2eta_highjet')
  Eff_l2eta_lowpv=TEfficiency(h1_l2eta_lowpv, h1_pre_l2eta_lowpv)
  Eff_l2eta_lowpv.SetTitle('Eff l2eta_lowpv')
  Eff_l2eta_highpv=TEfficiency(h1_l2eta_highpv, h1_pre_l2eta_highpv)
  Eff_l2eta_highpv.SetTitle('Eff l2eta_highpv')
  Eff_l2eta_lowMET=TEfficiency(h1_l2eta_lowMET, h1_pre_l2eta_lowMET)
  Eff_l2eta_lowMET.SetTitle('Eff l2eta_lowMET')
  Eff_l2eta_highMET=TEfficiency(h1_l2eta_highMET, h1_pre_l2eta_highMET)
  Eff_l2eta_highMET.SetTitle('Eff l2eta_highMET')

  Eff_njet=TEfficiency(h1_njet, h1_pre_njet)
  Eff_njet.SetTitle('Eff njet')
  Eff_met=TEfficiency(h1_met, h1_pre_met)
  Eff_met.SetTitle('Eff met')
  Eff_pu=TEfficiency(h1_pu, h1_pre_pu)
  Eff_pu.SetTitle('Eff pu')
  Eff_putrue=TEfficiency(h1_putrue, h1_pre_putrue)
  Eff_pu.SetTitle('Eff putrue')

  h2_l1pteta.Divide(h2_pre_l1pteta)
  h2_l1pteta_lowjet.Divide(h2_pre_l1pteta_lowjet)
  h2_l1pteta_highjet.Divide(h2_pre_l1pteta_highjet)
  h2_l1pteta_lowpv.Divide(h2_pre_l1pteta_lowpv)
  h2_l1pteta_highpv.Divide(h2_pre_l1pteta_highpv)
  h2_l1pteta_lowMET.Divide(h2_pre_l1pteta_lowMET)
  h2_l1pteta_highMET.Divide(h2_pre_l1pteta_highMET)

  h2_l2pteta.Divide(h2_pre_l2pteta)
  h2_l2pteta_lowjet.Divide(h2_pre_l2pteta_lowjet)
  h2_l2pteta_highjet.Divide(h2_pre_l2pteta_highjet)
  h2_l2pteta_lowpv.Divide(h2_pre_l2pteta_lowpv)
  h2_l2pteta_highpv.Divide(h2_pre_l2pteta_highpv)
  h2_l2pteta_lowMET.Divide(h2_pre_l2pteta_lowMET)
  h2_l2pteta_highMET.Divide(h2_pre_l2pteta_highMET)

  print 'test!!!'
  print h2_pre_l1l2pt.GetBinContent(2,2)
  print h2_l1l2pt.GetBinContent(2,2)
  h2_l1l2pt.Divide(h2_pre_l1l2pt)
  h2_l1l2pt_lowjet.Divide(h2_pre_l1l2pt_lowjet)
  h2_l1l2pt_highjet.Divide(h2_pre_l1l2pt_highjet)
  h2_l1l2pt_lowpv.Divide(h2_pre_l1l2pt_lowpv)
  h2_l1l2pt_highpv.Divide(h2_pre_l1l2pt_highpv)
  h2_l1l2pt_lowMET.Divide(h2_pre_l1l2pt_lowMET)
  h2_l1l2pt_highMET.Divide(h2_pre_l1l2pt_highMET)

  h2_l1l2eta.Divide(h2_pre_l1l2eta)
  h2_l1l2eta_lowjet.Divide(h2_pre_l1l2eta_lowjet)
  h2_l1l2eta_highjet.Divide(h2_pre_l1l2eta_highjet)
  h2_l1l2eta_lowpv.Divide(h2_pre_l1l2eta_lowpv)
  h2_l1l2eta_highpv.Divide(h2_pre_l1l2eta_highpv)
  h2_l1l2eta_lowMET.Divide(h2_pre_l1l2eta_lowMET)
  h2_l1l2eta_highMET.Divide(h2_pre_l1l2eta_highMET)
  
  Eff_mettrigger=TEfficiency(pass_met_trigger, all_events2)
  Eff_leptrigger=TEfficiency(pass_lep_trigger, all_events1)
  Eff_lepmettrigger=TEfficiency(pass_lepmet_trigger, all_events3)

  lepeff=Eff_leptrigger.GetEfficiency(1)
  lepeff_err=max(Eff_leptrigger.GetEfficiencyErrorUp(1), Eff_leptrigger.GetEfficiencyErrorLow(1))
  meteff=Eff_mettrigger.GetEfficiency(1)
  meteff_err=max(Eff_mettrigger.GetEfficiencyErrorUp(1), Eff_mettrigger.GetEfficiencyErrorLow(1))
  lepmeteff=Eff_lepmettrigger.GetEfficiency(1)
  lepmeteff_err=max(Eff_lepmettrigger.GetEfficiencyErrorUp(1), Eff_lepmettrigger.GetEfficiencyErrorLow(1))
  alpha=(lepeff*meteff)/lepmeteff
  alphaerr=sqrt(lepeff_err*lepeff_err*meteff*meteff + lepeff*lepeff*meteff_err*meteff_err + lepeff*lepeff*meteff*meteff*lepmeteff_err*lepmeteff_err/(lepmeteff*lepmeteff))/lepmeteff

  print 'lep trigger eff:', lepeff,'+-',lepeff_err
  print 'met trigger eff:', meteff,'+-',meteff_err
  print 'lepmet trigger eff:', lepmeteff,'+-',lepmeteff_err
  print 'alpha:', alpha,'+-',alphaerr

  fileout.cd()
  Eff_lepmettrigger.Write()
  Eff_leptrigger.Write()
  Eff_mettrigger.Write()
  Eff_njet.Write()
  Eff_met.Write()
  Eff_pu.Write()
  Eff_putrue.Write()

  Eff_l1pt.Write()
  Eff_l1pt_lowjet.Write()
  Eff_l1pt_highjet.Write()
  Eff_l1pt_lowpv.Write()
  Eff_l1pt_highpv.Write()
  Eff_l1pt_lowMET.Write()
  Eff_l1pt_highMET.Write()

  Eff_l1eta.Write()
  Eff_l1eta_lowjet.Write()
  Eff_l1eta_highjet.Write()
  Eff_l1eta_lowpv.Write()
  Eff_l1eta_highpv.Write()
  Eff_l1eta_lowMET.Write()
  Eff_l1eta_highMET.Write()

  Eff_l2pt.Write()
  Eff_l2pt_lowjet.Write()
  Eff_l2pt_highjet.Write()
  Eff_l2pt_lowpv.Write()
  Eff_l2pt_highpv.Write()
  Eff_l2pt_lowMET.Write()
  Eff_l2pt_highMET.Write()

  Eff_l2eta.Write()
  Eff_l2eta_lowjet.Write()
  Eff_l2eta_highjet.Write()
  Eff_l2eta_lowpv.Write()
  Eff_l2eta_highpv.Write()
  Eff_l2eta_lowMET.Write()
  Eff_l2eta_highMET.Write()

  h2_l1l2pt.Write()
  h2_l1l2pt_lowjet.Write()
  h2_l1l2pt_highjet.Write()
  h2_l1l2pt_lowpv.Write()
  h2_l1l2pt_highpv.Write()
  h2_l1l2pt_lowMET.Write()
  h2_l1l2pt_highMET.Write()

  h2_l1l2eta.Write()
  h2_l1l2eta_lowjet.Write()
  h2_l1l2eta_highjet.Write()
  h2_l1l2eta_lowpv.Write()
  h2_l1l2eta_highpv.Write()
  h2_l1l2eta_lowMET.Write()
  h2_l1l2eta_highMET.Write()

  h2_l1pteta.Write()
  h2_l1pteta_lowjet.Write()
  h2_l1pteta_highjet.Write()
  h2_l1pteta_lowpv.Write()
  h2_l1pteta_highpv.Write()
  h2_l1pteta_lowMET.Write()
  h2_l1pteta_highMET.Write()

  h2_l2pteta.Write()
  h2_l2pteta_lowjet.Write()
  h2_l2pteta_highjet.Write()
  h2_l2pteta_lowpv.Write()
  h2_l2pteta_highpv.Write()
  h2_l2pteta_lowMET.Write()
  h2_l2pteta_highMET.Write()

  fileout.Close()

def main():
#  calc('B',22)
#  calc('B',24)
#  calc('B',26)
#  calc('C',22)
#  calc('C',24)
#  calc('C',26)
#  calc('D',22)
#  calc('D',24)
#  calc('D',26)
#  calc('E',22)
#  calc('E',24)
#  calc('E',26)
#  calc('F',22)
#  calc('F',24)
#  calc('F',26)
  calc('ALL',22)
  calc('ALL',24)
  calc('ALL',26)
#  calc('TTto2L',22)
#  calc('TTto2L',24)
#  calc('TTto2L',26)
#  calc('TTto1L',22)
#  calc('TTto1L',24)
#  calc('TTto1L',26)

if __name__ == "__main__":
  sys.exit(main())
