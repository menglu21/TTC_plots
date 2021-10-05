#include "ROOT/RDataFrame.hxx"
#include "TString.h"
#include "TFile.h"
#include "TH2D.h"
#include "TMath.h"

#include "ROOT/RVec.hxx"

using namespace ROOT::VecOps;
using rvec_f = const RVec<float> &;

TFile*f=TFile::Open("TriggerSF_2017UL.root");
TH2D*h1_ee=(TH2D*)f->Get("h2D_SF_ee_lep1pteta");
TH2D*h2_ee=(TH2D*)f->Get("h2D_SF_ee_lep2pteta");
TH2D*h1_mm=(TH2D*)f->Get("h2D_SF_mumu_lep1pteta");
TH2D*h2_mm=(TH2D*)f->Get("h2D_SF_mumu_lep2pteta");
TH2D*h1_em=(TH2D*)f->Get("h2D_SF_emu_lep1pteta");
TH2D*h2_em=(TH2D*)f->Get("h2D_SF_emu_lep2pteta");

float trigger_sf_ee(float l1_pt, float l2_pt, float l1_eta, float l2_eta){
	if(l1_pt>200) l1_pt=199;
	if(l2_pt>200) l2_pt=199;
	float sf_l1=h1_ee->GetBinContent(h1_ee->FindBin(l1_pt,fabs(l1_eta)));
	float sf_l2=h2_ee->GetBinContent(h2_ee->FindBin(l2_pt,fabs(l2_eta)));
	return sf_l1*sf_l2;
}

float trigger_sf_mm(float l1_pt, float l2_pt, float l1_eta, float l2_eta){
	if(l1_pt>200) l1_pt=199;
	if(l2_pt>200) l2_pt=199;
	float sf_l1=h1_mm->GetBinContent(h1_mm->FindBin(l1_pt,fabs(l1_eta)));
	float sf_l2=h2_mm->GetBinContent(h2_mm->FindBin(l2_pt,fabs(l2_eta)));
	return sf_l1*sf_l2;
}

float trigger_sf_em(float l1_pt, float l2_pt, float l1_eta, float l2_eta){
	if(l1_pt>200) l1_pt=199;
	if(l2_pt>200) l2_pt=199;
	float sf_l1=h1_em->GetBinContent(h1_em->FindBin(l1_pt,fabs(l1_eta)));
	float sf_l2=h2_em->GetBinContent(h2_em->FindBin(l2_pt,fabs(l2_eta)));
	return sf_l1*sf_l2;
}

float extract_jet_pt(rvec_f pt_arr, int jid){
	return pt_arr[jid];
}

float extract_jet_eta(rvec_f eta_arr, int jid){
	return eta_arr[jid];
}

float extract_jet_phi(rvec_f phi_arr, int jid){
	return phi_arr[jid];
}

float extract_jet_mass(rvec_f mass_arr, int jid){
	return mass_arr[jid];
}
