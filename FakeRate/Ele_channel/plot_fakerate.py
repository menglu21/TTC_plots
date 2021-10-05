import ROOT
import numpy as np
from ROOT import kFALSE

import CMSTDRStyle
CMSTDRStyle.setTDRStyle().cd()
import CMSstyle
from array import array

def draw_plots(hist_nume =[], hist_deno =[]):

	fileout = ROOT.TFile('allhist.root', 'RECREATE')
        fileout.cd()
        for i in range(0,len(hist_nume)):
                hist_nume[i].Write()
                hist_deno[i].Write()
        fileout.Close()

	h_data_denominator=hist_deno[0]
	h_DY_denominator=hist_deno[1]
	h_WJet_denominator=hist_deno[2]

	h_data_numerator=hist_nume[0]
	h_DY_numerator=hist_nume[1]
	h_WJet_numerator=hist_nume[2]

	c1 = ROOT.TCanvas('','',800,600)
	pad = ROOT.TPad()
	pad.Draw()

	h_nume=h_data_numerator.Clone()
	h_nume.Add(h_DY_numerator)
	h_nume.Add(h_WJet_numerator)

	h_deno=h_data_denominator.Clone()
	h_deno.Add(h_DY_denominator)
	h_deno.Add(h_WJet_denominator)

	h_nume.SetName('fakerate')
	h_nume.GetXaxis().SetTitle("#||{#eta}")
	h_nume.GetYaxis().SetTitle("P_{T} [GeV]")
	h_nume.GetXaxis().SetTitleSize(0.05)
	h_nume.GetYaxis().SetTitleSize(0.05)
	h_nume.Divide(h_deno)
	h_nume.Draw('COL TEXT E')

	fileout = ROOT.TFile('fr.root', 'RECREATE')
	fileout.cd()
	h_nume.Write()
	fileout.Close()


	CMSstyle.SetStyle(pad)
	pad.SetRightMargin(0.15)
	c1.SetGridx(False);
	c1.SetGridy(False);
	c1.Update()
	c1.SaveAs('fakerate.pdf')
	c1.SaveAs('fakerate.png')
	return c1
	pad.Close()
	del hist_nume
	del hist_deno
