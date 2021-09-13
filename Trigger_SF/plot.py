import ROOT
import sys
from ROOT import TFile, TH1F, TH2D, TCanvas, TLegend, TPad, TEfficiency
import numpy as np

import CMSTDRStyle
CMSTDRStyle.setTDRStyle().cd()
import CMSstyle
from array import array

def draw_1dplot(plotType, channel, valuable):
  filenames = []
  files = []
  histos = []

  colors=[1,632,416,600,616,432,800]
  
  if (plotType=='ALL'):
    filenames.append('MET')
    filenames.append('TTto2L')
  if (plotType=='Separate'):
    filenames.append('METB')
    filenames.append('METC')
    filenames.append('METD')
    filenames.append('METE')
    filenames.append('METF')
    filenames.append('MET')
    filenames.append('TTto2L')
  
  if (channel=='ee'):
    for i in range(0,len(filenames)):
      files.append(TFile.Open(filenames[i]+'_ee.root'))
  elif (channel=='em'):
    for i in range(0,len(filenames)):
      files.append(TFile.Open(filenames[i]+'_em.root'))
  else:
    for i in range(0,len(filenames)):
      files.append(TFile.Open(filenames[i]+'_mm.root'))
  
  histotemp=TEfficiency()
  for i in range(0,len(files)):
    files[i].GetObject('pre_'+valuable+'_clone',histotemp)
    histotemp.SetNameTitle('','')
    histos.append(histotemp.Clone())
  
  c1 = TCanvas()
  pad = TPad()
  pad.Draw()
  for i in range(0,len(files)):
    histos[i].SetLineColor(colors[i])
    histos[i].SetMarkerStyle(20)
    histos[i].SetMarkerSize(0.5)
    histos[i].SetMarkerColor(colors[i])
    if i==0:
      #histos[i].Draw()
      gr=histos[i].CreateGraph()
      gr.SetMinimum(0.5)
      gr.SetMaximum(1.0)
      gr.Draw("AP")
    else:
      #histos[i].Draw('SAME')
      gr=histos[i].CreateGraph()
      gr.SetMinimum(0.5)
      gr.SetMaximum(1.0)
      gr.Draw('sameP')

  CMSstyle.SetStyle(pad)

  leg1=TLegend(0.5,0.2,0.65,0.2+0.05*len(files))
  for i in range(0,len(files)):
    leg1.AddEntry(histos[i],filenames[i])
  leg1.SetFillStyle(0)
  leg1.Draw('SAME')

  c1.Update()
  c1.SaveAs(valuable+'_'+plotType+'_'+channel+'.png')
  return c1
  pad.Close()

def draw_2dplot(filename1,filename2, channel, valuable, types):
  filein1=TFile.Open(filename1+'_'+channel+'.root')
  filein2=TFile.Open(filename2+'_'+channel+'.root')
  histotemp1=TH2D()
  histotemp2=TH2D()
  filein1.GetObject(valuable,histotemp1)
  filein2.GetObject(valuable,histotemp2)
  histotemp1.SetNameTitle('','')
  histotemp2.SetNameTitle('','')

  c1 = TCanvas()
  pad = TPad()
  pad.Draw()

  if (types=='eff'):
    histotemp1.Draw('COLZ TEXT E')
    CMSstyle.SetStyle(pad)
    pad.SetRightMargin(0.15)
    c1.SetGridx(False);
    c1.SetGridy(False);
    c1.Update()
    c1.SaveAs('Eff_'+filename1+'_'+channel+'_'+valuable+'.png')

  if (types=='sf'):
    histotemp1.Divide(histotemp2)
    histotemp1.Draw('COLZ TEXT E')
    if 'l1pteta' in valuable or 'l2pteta' in valuable:
      print histotemp1.GetBinContent(1,4),histotemp1.GetBinContent(2,4),histotemp1.GetBinContent(3,4),histotemp1.GetBinContent(4,4),histotemp1.GetBinContent(5,4),histotemp1.GetBinContent(6,4)
      print histotemp1.GetBinContent(1,3),histotemp1.GetBinContent(2,3),histotemp1.GetBinContent(3,3),histotemp1.GetBinContent(4,3),histotemp1.GetBinContent(5,3),histotemp1.GetBinContent(6,3)
      print histotemp1.GetBinContent(1,2),histotemp1.GetBinContent(2,2),histotemp1.GetBinContent(3,2),histotemp1.GetBinContent(4,2),histotemp1.GetBinContent(5,2),histotemp1.GetBinContent(6,2)
      print histotemp1.GetBinContent(1,1),histotemp1.GetBinContent(2,1),histotemp1.GetBinContent(3,1),histotemp1.GetBinContent(4,1),histotemp1.GetBinContent(5,1),histotemp1.GetBinContent(6,1)
    CMSstyle.SetStyle(pad)
    pad.SetRightMargin(0.15)
    c1.SetGridx(False);
    c1.SetGridy(False);
    c1.Update()
    c1.SaveAs('SF_'+'_'+channel+'_'+valuable+'.png')

  return c1
  pad.Close()

def main():
  app='_highpv'
  keys=['l1pt','l1eta','l2pt','l2eta']
  #keys=['l1pt','l1eta','l2pt','l2eta','njet','met']
  #keys=['l1pt','l1eta','l2pt','l2eta','njet','met','nvtx','pu','putrue']
  for i in range(len(keys)):
    c1=draw_1dplot('ALL','ee',keys[i]+app)
    c2=draw_1dplot('ALL','em',keys[i]+app)
    c3=draw_1dplot('ALL','mm',keys[i]+app)
    c4=draw_1dplot('Separate','ee',keys[i]+app)
    c5=draw_1dplot('Separate','em',keys[i]+app)
    c6=draw_1dplot('Separate','mm',keys[i]+app)

  tdkeys=['l1pteta','l2pteta','l1l2pt','l1l2eta']
  channels=['ee','em','mm']
  for i in range(len(tdkeys)):
    for j in range(len(channels)):
      ci=draw_2dplot('MET','TTto2L', channels[j], tdkeys[i]+app, 'sf')
      cj=draw_2dplot('MET','TTto2L', channels[j], tdkeys[i]+app, 'eff')
      ck=draw_2dplot('TTto2L','TTto2L', channels[j], tdkeys[i]+app, 'eff')

if __name__ == "__main__":
  sys.exit(main())
