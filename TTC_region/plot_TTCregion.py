import ROOT
import numpy as np
from ROOT import kFALSE

import CMSTDRStyle
CMSTDRStyle.setTDRStyle().cd()
import CMSstyle
from array import array

def set_axis(the_histo, coordinate, title, is_energy):

	if coordinate == 'x':
		axis = the_histo.GetXaxis()
	elif coordinate == 'y':
		axis = the_histo.GetYaxis()
	else:
		raise ValueError('x and y axis only')

	axis.SetLabelFont(42)
	axis.SetLabelOffset(0.015)
	axis.SetNdivisions(505)
	axis.SetTitleFont(42)
	axis.SetTitleOffset(1.15)
	axis.SetLabelSize(0.03)
	axis.SetTitleSize(0.04)
	if coordinate == 'x':
		axis.SetLabelSize(0.0)
		axis.SetTitleSize(0.0)
	if (coordinate == "y"):axis.SetTitleOffset(1.2)
	if is_energy:
		axis.SetTitle(title+' [GeV]')
	else:
		axis.SetTitle(title) 

def draw_plots(hist_array =[], draw_data=0, x_name='', isem=0):

	fileout = ROOT.TFile(x_name+'.root', 'RECREATE')
	fileout.cd()
	for i in range(0,len(hist_array)):
		hist_array[i].Write()
	fileout.Close()

	lumi=41480.
	DY = hist_array[0].Clone()
	DY.SetFillColor(ROOT.kRed)
	DY.Scale(lumi)

	WJet = hist_array[1].Clone()
	WJet.SetFillColor(ROOT.kBlue-7)
	WJet.Scale(lumi)

	VV = hist_array[2].Clone()
	VV.Add(hist_array[3])
	VV.Add(hist_array[4])
	VV.SetFillColor(ROOT.kCyan-7)
	VV.Scale(lumi)

	VVV = hist_array[5].Clone()
	VVV.Add(hist_array[6])
	VVV.Add(hist_array[7])
	VVV.Add(hist_array[8])
	VVV.SetFillColor(ROOT.kSpring-9)
	VVV.Scale(lumi)

	SingleTop = hist_array[9].Clone()
	SingleTop.Add(hist_array[10])
	SingleTop.Add(hist_array[11])
	SingleTop.Add(hist_array[12])
	SingleTop.Add(hist_array[13])
	SingleTop.SetFillColor(ROOT.kGray)
	SingleTop.Scale(lumi)

	ttXorXX = hist_array[14].Clone()
	ttXorXX.Add(hist_array[15])
	ttXorXX.Add(hist_array[16])
	ttXorXX.Add(hist_array[17])
	ttXorXX.Add(hist_array[18])
	ttXorXX.Add(hist_array[19])
	ttXorXX.Add(hist_array[20])
	ttXorXX.Add(hist_array[21])
	ttXorXX.SetFillColor(ROOT.kViolet-4)
	ttXorXX.Scale(lumi)

	tzq = hist_array[22].Clone()
	tzq.SetFillColor(ROOT.kYellow-4)
	tzq.Scale(lumi)

#	QCD = hist_array[23].Clone()
#	QCD.Add(hist_array[24])
#	QCD.Add(hist_array[25])
#	QCD.Add(hist_array[26])
#	QCD.Add(hist_array[27])
#	QCD.SetFillColor(ROOT.kOrange+1)
#	QCD.Scale(lumi)

	TT = hist_array[23].Clone()
	TT.Add(hist_array[24])
	TT.SetFillColor(ROOT.kBlue)
	TT.Scale(lumi)

	Data = hist_array[25].Clone()
	Data.Add(hist_array[26])
	if isem==1:
		Data.Add(hist_array[27])#if emu channel
	if not draw_data: Data.Reset('ICE')
	Data.SetMarkerStyle(20)
	Data.SetMarkerSize(0.85)
	Data.SetMarkerColor(1)
	Data.SetLineWidth(1)

	h_stack = ROOT.THStack()
	h_stack.Add(DY)
	h_stack.Add(TT)
	h_stack.Add(WJet)
	h_stack.Add(VV)
	h_stack.Add(VVV)
	h_stack.Add(SingleTop)
	h_stack.Add(ttXorXX)
	h_stack.Add(tzq)
#	h_stack.Add(QCD)
	max_yields = 0
	Nbins=h_stack.GetStack().Last().GetNbinsX()
	for i in range(1,Nbins+1):
		max_yields_temp = h_stack.GetStack().Last().GetBinContent(i)
		if max_yields_temp>max_yields:max_yields=max_yields_temp

	max_yields_data = 0
	for i in range(1,Nbins+1):
		max_yields_data_temp = Data.GetBinContent(i)
		if max_yields_data_temp>max_yields_data:max_yields_data=max_yields_data_temp

	h_stack.SetMaximum(max(max_yields, max_yields_data)*1.8)

	##MC error
	h_error = h_stack.GetStack().Last()
	h_error.SetBinErrorOption(ROOT.TH1.kPoisson);
	binsize = h_error.GetSize()-2;
	x = [];
	y = [];
	xerror_l = [];
	xerror_r = [];
	yerror_u = [];
	yerror_d = [];
	y_pad2 = [];
	y_pad2_error_u = [];
	y_pad2_error_d = [];
	for i in range(0,binsize):
		x.append(h_error.GetBinCenter(i+1))
		y.append(h_error.GetBinContent(i+1))
		y_pad2.append(1.0)
		xerror_l.append(0.5*h_error.GetBinWidth(i+1))
		xerror_r.append(0.5*h_error.GetBinWidth(i+1))
		yerror_u.append(h_error.GetBinErrorUp(i+1))
		yerror_d.append(h_error.GetBinErrorLow(i+1))
		if h_error.GetBinContent(i+1)<=0:
		  y_pad2_error_u.append(0)
		  y_pad2_error_d.append(0)
		else:
		  y_pad2_error_u.append(h_error.GetBinErrorUp(i+1)/(h_error.GetBinContent(i+1)))
		  y_pad2_error_d.append(h_error.GetBinErrorLow(i+1)/(h_error.GetBinContent(i+1)))
	gr = ROOT.TGraphAsymmErrors(len(x), np.array(x), np.array(y),np.array(xerror_l),np.array(xerror_r), np.array(yerror_d), np.array(yerror_u))
	gr_pad2 = ROOT.TGraphAsymmErrors(len(x), np.array(x), np.array(y_pad2),np.array(xerror_l),np.array(xerror_r), np.array(y_pad2_error_d), np.array(y_pad2_error_u))

	DY_yield =round(DY.Integral(),1)
	TT_yield =round(TT.Integral(),1)
	WJet_yield =round(WJet.Integral(),1)
	VV_yield =round(VV.Integral(),1)
	VVV_yield =round(VVV.Integral(),1)
	SingleTop_yield =round(SingleTop.Integral(),1)
	ttXorXX_yield =round(ttXorXX.Integral(),1)
	tzq_yield =round(tzq.Integral(),1)
#	QCD_yield =round(QCD.Integral(),1)
	Data_yield = round(Data.Integral())

	c = ROOT.TCanvas()
	pad1 = ROOT.TPad('pad1','',0.00, 0.22, 0.99, 0.99)
	pad2 = ROOT.TPad('pad1','',0.00, 0.00, 0.99, 0.22)
	pad1.SetBottomMargin(0.025);
        pad2.SetTopMargin(0.035);
        pad2.SetBottomMargin(0.45);
	pad1.Draw()
	pad2.Draw()
	pad1.cd()
	h_stack.Draw('HIST')
	Data.Draw("SAME pe")

	gr.SetFillColor(1)
	gr.SetFillStyle(3005)
	gr.Draw("SAME 2")
	if 'ttc_l1_pt' in x_name:set_axis(h_stack,'x', 'p_{T}(Leading lepton)', True)
	if 'ttc_l1_eta' in x_name:set_axis(h_stack,'x', '#eta(Leading lepton)', False)
	if 'ttc_l1_phi' in x_name:set_axis(h_stack,'x', '#phi(leading lepton)', False)
	if 'ttc_l2_pt' in x_name:set_axis(h_stack,'x', 'p_{T}(Subleading lepton)', True)
	if 'ttc_l2_eta' in x_name:set_axis(h_stack,'x', '#eta(Subleading lepton)', False)
	if 'ttc_l2_phi' in x_name:set_axis(h_stack,'x', '#phi(Subleading lepton)', False)
	if 'ttc_mll' in x_name:set_axis(h_stack,'x', 'M_{ll}', True)
	if 'ttc_drll' in x_name:set_axis(h_stack,'x', '#DeltaR_{ll}', False)
	if 'ttc_dphill' in x_name:set_axis(h_stack,'x', '#Delta#phi_{ll}', False)
	if 'ttc_met' in x_name:set_axis(h_stack,'x', 'MET', True)
	if 'ttc_met_phi' in x_name:set_axis(h_stack,'x', '#phi(MET)', False)
	if 'j1_pt' in x_name:set_axis(h_stack,'x', 'p_{T}(j1)', True)
	if 'j1_eta' in x_name:set_axis(h_stack,'x', '#eta(j1)', False)
	if 'j1_phi' in x_name:set_axis(h_stack,'x', '#phi(j1)', False)
	if 'j1_mass' in x_name:set_axis(h_stack,'x', 'M(j1)', True)
	if 'j2_pt' in x_name:set_axis(h_stack,'x', 'p_{T}(j2)', True)
	if 'j2_eta' in x_name:set_axis(h_stack,'x', '#eta(j2)', False)
	if 'j2_phi' in x_name:set_axis(h_stack,'x', '#phi(j2)', False)
	if 'j2_mass' in x_name:set_axis(h_stack,'x', 'M(j2)', True)
	if 'j3_pt' in x_name:set_axis(h_stack,'x', 'p_{T}(j3)', True)
	if 'j3_eta' in x_name:set_axis(h_stack,'x', '#eta(j3)', False)
	if 'j3_phi' in x_name:set_axis(h_stack,'x', '#phi(j3)', False)
	if 'j3_mass' in x_name:set_axis(h_stack,'x', 'M(j3)', True)
	if 'ttc_mllj1' in x_name:set_axis(h_stack,'x', 'M(ll, j1)', True)
	if 'ttc_mllj2' in x_name:set_axis(h_stack,'x', 'M(ll, j2)', True)
	if 'ttc_mllj3' in x_name:set_axis(h_stack,'x', 'M(ll, j3)', True)
	if 'ttc_dr_l1j1' in x_name:set_axis(h_stack,'x', '#DeltaR(l1, j1)', False)
	if 'ttc_dr_l1j2' in x_name:set_axis(h_stack,'x', '#DeltaR(l1, j2)', False)
	if 'ttc_dr_l1j3' in x_name:set_axis(h_stack,'x', '#DeltaR(l1, j3)', False)
	if 'ttc_dr_l2j1' in x_name:set_axis(h_stack,'x', '#DeltaR(l2, j1)', False)
	if 'ttc_dr_l2j2' in x_name:set_axis(h_stack,'x', '#DeltaR(l2, j2)', False)
	if 'ttc_dr_l2j3' in x_name:set_axis(h_stack,'x', '#DeltaR(l2, j3)', False)
	if 'n_tight_jet' in x_name:set_axis(h_stack,'x', 'Jet multiplicity', False)

	if 'DY_l1_pt' in x_name:set_axis(h_stack,'x', 'p_{T}(Leading lepton)', True)
	if 'DY_l1_eta' in x_name:set_axis(h_stack,'x', '#eta(Leading lepton)', False)
	if 'DY_l1_phi' in x_name:set_axis(h_stack,'x', '#phi(Leading lepton)', False)
	if 'DY_l2_pt' in x_name:set_axis(h_stack,'x', 'p_{T}(Subleading lepton)', True)
	if 'DY_l2_eta' in x_name:set_axis(h_stack,'x', '#eta(Subleading lepton)', False)
	if 'DY_l2_phi' in x_name:set_axis(h_stack,'x', '#phi(Subleading lepton)', False)
	if 'DY_z_mass' in x_name:set_axis(h_stack,'x', 'M(Z)', True)
	if 'DY_z_pt' in x_name:set_axis(h_stack,'x', 'p_{T}(Z)', True)
	if 'DY_z_eta' in x_name:set_axis(h_stack,'x', '#eta(Z)', False)
	if 'DY_z_phi' in x_name:set_axis(h_stack,'x', '#phi(Z)', False)
	# WZ region
	if 'wl_pt' in x_name:set_axis(h_stack,'x', 'p_{T}(W lep)', True)
	if 'wl_eta' in x_name:set_axis(h_stack,'x', '#eta(W lep)', False)
	if 'zl1_pt' in x_name:set_axis(h_stack,'x', 'p_{T}(Z l1)', True)
	if 'zl1_eta' in x_name:set_axis(h_stack,'x', '#eta(Z l1)', False)
	if 'zl2_pt' in x_name:set_axis(h_stack,'x', 'p_{T}(Z l2)', True)
	if 'zl2_eta' in x_name:set_axis(h_stack,'x', '#eta(Z l2)', False)
	#if 'met' in x_name:set_axis(h_stack,'x', 'MET', True)
	if 'zmass' in x_name:set_axis(h_stack,'x', 'M(Z)', True)
	
	set_axis(h_stack,'y', 'Event/Bin', False)

	CMSstyle.SetStyle(pad1)

	##legend
	leg1 = ROOT.TLegend(0.66, 0.75, 0.94, 0.88)
        leg2 = ROOT.TLegend(0.44, 0.75, 0.64, 0.88)
        leg3 = ROOT.TLegend(0.17, 0.75, 0.40, 0.88)
        leg1.SetMargin(0.4)
        leg2.SetMargin(0.4)
        leg3.SetMargin(0.4)

        leg3.AddEntry(DY,'DY ['+str(DY_yield)+']','f')
        leg3.AddEntry(gr,'Stat. unc','f')
        leg3.AddEntry(Data,'Data ['+str(Data_yield)+']','pe')
        leg2.AddEntry(TT,'TT ['+str(TT_yield)+']','f')
        leg2.AddEntry(WJet,'WJet ['+str(WJet_yield)+']','f')
        leg2.AddEntry(VV,'VV ['+str(VV_yield)+']','f')
        leg1.AddEntry(VVV,'VVV ['+str(VVV_yield)+']','f')
        leg1.AddEntry(SingleTop,'SingleTop ['+str(SingleTop_yield)+']','f')
        leg1.AddEntry(ttXorXX,'TTXorXX ['+str(ttXorXX_yield)+']','f')
        leg1.AddEntry(tzq,'tzq ['+str(tzq_yield)+']','f')
#        leg1.AddEntry(QCD,'QCD ['+str(QCD_yield)+']','f')
        leg1.SetFillColor(ROOT.kWhite)
        leg1.Draw('same')
        leg2.SetFillColor(ROOT.kWhite);
        leg2.Draw('same');
        leg3.SetFillColor(ROOT.kWhite);
        leg3.Draw('same');

	pad2.cd()
	hMC = h_stack.GetStack().Last()
	hData = Data.Clone()
	hData.Divide(hMC)
	hData.SetMarkerStyle(20)
        hData.SetMarkerSize(0.85)
        hData.SetMarkerColor(1)
        hData.SetLineWidth(1)

	hData.GetYaxis().SetTitle("Data/Pred.")
	hData.GetXaxis().SetTitle(h_stack.GetXaxis().GetTitle())
        hData.GetYaxis().CenterTitle()
	hData.SetMaximum(1.5)
	hData.SetMinimum(0.5)
        hData.GetYaxis().SetNdivisions(4,kFALSE)
        hData.GetYaxis().SetTitleOffset(0.3)
        hData.GetYaxis().SetTitleSize(0.13)
        hData.GetYaxis().SetLabelSize(0.1)
        hData.GetXaxis().SetTitleSize(0.14)
        hData.GetXaxis().SetLabelSize(0.1)
	hData.Draw()

	gr_pad2.SetFillColor(1)
        gr_pad2.SetFillStyle(3005)
        gr_pad2.Draw("SAME 2")

	c.Update()
	c.SaveAs(x_name+'.pdf')
	c.SaveAs(x_name+'.png')
	return c
	pad1.Close()
	pad2.Close()
	del hist_array
