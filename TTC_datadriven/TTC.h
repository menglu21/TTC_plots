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

TFile*f_m=TFile::Open("Mu_Fake_Rate_2D.root");
TFile*f_e=TFile::Open("Ele_Fake_Rate_2D.root");
TH2D*h_m=(TH2D*)f_m->Get("fakerate");
TH2D*h_e=(TH2D*)f_e->Get("fakerate");

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

float fakelepweight_ee_data(bool ttc_1P1F, bool ttc_0P2F, bool ttc_lep1_faketag, float l1_pt, float l1_eta, float l2_pt, float l2_eta){
        float w_temp=1.0;
        float fakerate1=1.0;
        float fakerate2=1.0;
        int BinX = 0;
        int BinY = 0;
        if(ttc_1P1F){
            if(ttc_lep1_faketag){
                BinX = h_e->GetXaxis()->FindBin(fabs(l1_eta));
                BinY = h_e->GetYaxis()->FindBin(l1_pt);
                if (BinX > h_e.GetNbinsX()) BinX = h_e.GetNbinsX();
                if (BinY > h_e.GetNbinsY()) BinY = h_e.GetNbinsY();
                fakerate1=h_e->GetBinContent(BinX, BinY);
            }
            else {
                BinX = h_e->GetXaxis()->FindBin(fabs(l2_eta));
                BinY = h_e->GetYaxis()->FindBin(l2_pt);
                if (BinX > h_e.GetNbinsX()) BinX = h_e.GetNbinsX();
                if (BinY > h_e.GetNbinsY()) BinY = h_e.GetNbinsY();
                fakerate1=h_e->GetBinContent(BinX, BinY);
            }
            w_temp=fakerate1/(1-fakerate1);
        }
        if(ttc_0P2F){
            BinX = h_e->GetXaxis()->FindBin(fabs(l1_eta));
            BinY = h_e->GetYaxis()->FindBin(l1_pt);
            if (BinX > h_e.GetNbinsX()) BinX = h_e.GetNbinsX();
            if (BinY > h_e.GetNbinsY()) BinY = h_e.GetNbinsY();
            fakerate1=h_e->GetBinContent(BinX, BinY);

            BinX = h_e->GetXaxis()->FindBin(fabs(l2_eta));
            BinY = h_e->GetYaxis()->FindBin(l2_pt);
            if (BinX > h_e.GetNbinsX()) BinX = h_e.GetNbinsX();
            if (BinY > h_e.GetNbinsY()) BinY = h_e.GetNbinsY();
            fakerate2=h_e->GetBinContent(BinX, BinY);

            w_temp=-1*fakerate1*fakerate2/((1-fakerate1)*(1-fakerate2));
        }
        return w_temp;
}

float fakelepweight_em_data(bool ttc_1P1F, bool ttc_0P2F, bool ttc_lep1_faketag, float l1_pt, float l1_eta, float l2_pt, float l2_eta){
        float w_temp=1.0;
        float fakerate1=1.0;
        float fakerate2=1.0;
        int BinX = 0;
        int BinY = 0;
        if(ttc_1P1F){
            if(ttc_lep1_faketag){
                BinX = h_m->GetXaxis()->FindBin(fabs(l1_eta));
                BinY = h_m->GetYaxis()->FindBin(l1_pt);
                if (BinX > h_m.GetNbinsX()) BinX = h_m.GetNbinsX();
                if (BinY > h_m.GetNbinsY()) BinY = h_m.GetNbinsY();
                fakerate1=h_m->GetBinContent(BinX, BinY);
            }
            else {
                BinX = h_e->GetXaxis()->FindBin(fabs(l2_eta));
                BinY = h_e->GetYaxis()->FindBin(l2_pt);
                if (BinX > h_e.GetNbinsX()) BinX = h_e.GetNbinsX();
                if (BinY > h_e.GetNbinsY()) BinY = h_e.GetNbinsY();
                fakerate1=h_e->GetBinContent(BinX, BinY);
            }
            w_temp=fakerate1/(1-fakerate1);
        }
        if(ttc_0P2F){
            BinX = h_m->GetXaxis()->FindBin(fabs(l1_eta));
            BinY = h_m->GetYaxis()->FindBin(l1_pt);
            if (BinX > h_m.GetNbinsX()) BinX = h_m.GetNbinsX();
            if (BinY > h_m.GetNbinsY()) BinY = h_m.GetNbinsY();
            fakerate1=h_m->GetBinContent(BinX, BinY);

            BinX = h_e->GetXaxis()->FindBin(fabs(l2_eta));
            BinY = h_e->GetYaxis()->FindBin(l2_pt);
            if (BinX > h_e.GetNbinsX()) BinX = h_e.GetNbinsX();
            if (BinY > h_e.GetNbinsY()) BinY = h_e.GetNbinsY();
            fakerate2=h_e->GetBinContent(BinX, BinY);

            w_temp=-1*fakerate1*fakerate2/((1-fakerate1)*(1-fakerate2));
        }
        return w_temp;
}

float fakelepweight_mm_data(bool ttc_1P1F, bool ttc_0P2F, bool ttc_lep1_faketag, float l1_pt, float l1_eta, float l2_pt, float l2_eta){
        float w_temp=1.0;
        float fakerate1=1.0;
        float fakerate2=1.0;
        int BinX = 0;
        int BinY = 0;
        if(ttc_1P1F){
            if(ttc_lep1_faketag){
                BinX = h_m->GetXaxis()->FindBin(fabs(l1_eta));
                BinY = h_m->GetYaxis()->FindBin(l1_pt);
                if (BinX > h_m.GetNbinsX()) BinX = h_m.GetNbinsX();
                if (BinY > h_m.GetNbinsY()) BinY = h_m.GetNbinsY();
                fakerate1=h_m->GetBinContent(BinX, BinY);
            }
            else {
                BinX = h_m->GetXaxis()->FindBin(fabs(l2_eta));
                BinY = h_m->GetYaxis()->FindBin(l2_pt);
                if (BinX > h_m.GetNbinsX()) BinX = h_m.GetNbinsX();
                if (BinY > h_m.GetNbinsY()) BinY = h_m.GetNbinsY();
                fakerate1=h_m->GetBinContent(BinX, BinY);
            }
            w_temp=fakerate1/(1-fakerate1);
        }
        if(ttc_0P2F){
            BinX = h_m->GetXaxis()->FindBin(fabs(l1_eta));
            BinY = h_m->GetYaxis()->FindBin(l1_pt);
            if (BinX > h_m.GetNbinsX()) BinX = h_m.GetNbinsX();
            if (BinY > h_m.GetNbinsY()) BinY = h_m.GetNbinsY();
            fakerate1=h_m->GetBinContent(BinX, BinY);

            BinX = h_m->GetXaxis()->FindBin(fabs(l2_eta));
            BinY = h_m->GetYaxis()->FindBin(l2_pt);
            if (BinX > h_m.GetNbinsX()) BinX = h_m.GetNbinsX();
            if (BinY > h_m.GetNbinsY()) BinY = h_m.GetNbinsY();
            fakerate2=h_m->GetBinContent(BinX, BinY);

            w_temp=-1*fakerate1*fakerate2/((1-fakerate1)*(1-fakerate2));
        }
        return w_temp;
}

float fakelepweight_ee_mc(bool ttc_1P1F, bool ttc_0P2F, bool ttc_lep1_faketag, float l1_pt, float l1_eta, float l2_pt, float l2_eta){
        float w_temp=1.0;
        float fakerate1=1.0;
        float fakerate2=1.0;
        int BinX = 0;
        int BinY = 0;
        if(ttc_1P1F){
            if(ttc_lep1_faketag){
                BinX = h_e->GetXaxis()->FindBin(fabs(l1_eta));
                BinY = h_e->GetYaxis()->FindBin(l1_pt);
                if (BinX > h_e.GetNbinsX()) BinX = h_e.GetNbinsX();
                if (BinY > h_e.GetNbinsY()) BinY = h_e.GetNbinsY();
                fakerate1=h_e->GetBinContent(BinX, BinY);
            }
            else {
                BinX = h_e->GetXaxis()->FindBin(fabs(l2_eta));
                BinY = h_e->GetYaxis()->FindBin(l2_pt);
                if (BinX > h_e.GetNbinsX()) BinX = h_e.GetNbinsX();
                if (BinY > h_e.GetNbinsY()) BinY = h_e.GetNbinsY();
                fakerate1=h_e->GetBinContent(BinX, BinY);
            }
            w_temp=-1*fakerate1/(1-fakerate1);
        }
        if(ttc_0P2F){
            BinX = h_e->GetXaxis()->FindBin(fabs(l1_eta));
            BinY = h_e->GetYaxis()->FindBin(l1_pt);
            if (BinX > h_e.GetNbinsX()) BinX = h_e.GetNbinsX();
            if (BinY > h_e.GetNbinsY()) BinY = h_e.GetNbinsY();
            fakerate1=h_e->GetBinContent(BinX, BinY);

            BinX = h_e->GetXaxis()->FindBin(fabs(l2_eta));
            BinY = h_e->GetYaxis()->FindBin(l2_pt);
            if (BinX > h_e.GetNbinsX()) BinX = h_e.GetNbinsX();
            if (BinY > h_e.GetNbinsY()) BinY = h_e.GetNbinsY();
            fakerate2=h_e->GetBinContent(BinX, BinY);

            w_temp=fakerate1*fakerate2/((1-fakerate1)*(1-fakerate2));
        }
        return w_temp;
}

float fakelepweight_em_mc(bool ttc_1P1F, bool ttc_0P2F, bool ttc_lep1_faketag, float l1_pt, float l1_eta, float l2_pt, float l2_eta){
        float w_temp=1.0;
        float fakerate1=1.0;
        float fakerate2=1.0;
        int BinX = 0;
        int BinY = 0;
        if(ttc_1P1F){
            if(ttc_lep1_faketag){
                BinX = h_m->GetXaxis()->FindBin(fabs(l1_eta));
                BinY = h_m->GetYaxis()->FindBin(l1_pt);
                if (BinX > h_m.GetNbinsX()) BinX = h_m.GetNbinsX();
                if (BinY > h_m.GetNbinsY()) BinY = h_m.GetNbinsY();
                fakerate1=h_m->GetBinContent(BinX, BinY);
            }
            else {
                BinX = h_e->GetXaxis()->FindBin(fabs(l2_eta));
                BinY = h_e->GetYaxis()->FindBin(l2_pt);
                if (BinX > h_e.GetNbinsX()) BinX = h_e.GetNbinsX();
                if (BinY > h_e.GetNbinsY()) BinY = h_e.GetNbinsY();
                fakerate1=h_e->GetBinContent(BinX, BinY);
            }
            w_temp=-1*fakerate1/(1-fakerate1);
        }
        if(ttc_0P2F){
            BinX = h_m->GetXaxis()->FindBin(fabs(l1_eta));
            BinY = h_m->GetYaxis()->FindBin(l1_pt);
            if (BinX > h_m.GetNbinsX()) BinX = h_m.GetNbinsX();
            if (BinY > h_m.GetNbinsY()) BinY = h_m.GetNbinsY();
            fakerate1=h_m->GetBinContent(BinX, BinY);

            BinX = h_e->GetXaxis()->FindBin(fabs(l2_eta));
            BinY = h_e->GetYaxis()->FindBin(l2_pt);
            if (BinX > h_e.GetNbinsX()) BinX = h_e.GetNbinsX();
            if (BinY > h_e.GetNbinsY()) BinY = h_e.GetNbinsY();
            fakerate2=h_e->GetBinContent(BinX, BinY);

            w_temp=fakerate1*fakerate2/((1-fakerate1)*(1-fakerate2));
        }
        return w_temp;
}

float fakelepweight_mm_mc(bool ttc_1P1F, bool ttc_0P2F, bool ttc_lep1_faketag, float l1_pt, float l1_eta, float l2_pt, float l2_eta){
        float w_temp=1.0;
        float fakerate1=1.0;
        float fakerate2=1.0;
        int BinX = 0;
        int BinY = 0;
        if(ttc_1P1F){
            if(ttc_lep1_faketag){
                BinX = h_m->GetXaxis()->FindBin(fabs(l1_eta));
                BinY = h_m->GetYaxis()->FindBin(l1_pt);
                if (BinX > h_m.GetNbinsX()) BinX = h_m.GetNbinsX();
                if (BinY > h_m.GetNbinsY()) BinY = h_m.GetNbinsY();
                fakerate1=h_m->GetBinContent(BinX, BinY);
            }
            else {
                BinX = h_m->GetXaxis()->FindBin(fabs(l2_eta));
                BinY = h_m->GetYaxis()->FindBin(l2_pt);
                if (BinX > h_m.GetNbinsX()) BinX = h_m.GetNbinsX();
                if (BinY > h_m.GetNbinsY()) BinY = h_m.GetNbinsY();
                fakerate1=h_m->GetBinContent(BinX, BinY);
            }
            w_temp=-1*fakerate1/(1-fakerate1);
        }
        if(ttc_0P2F){
            BinX = h_m->GetXaxis()->FindBin(fabs(l1_eta));
            BinY = h_m->GetYaxis()->FindBin(l1_pt);
            if (BinX > h_m.GetNbinsX()) BinX = h_m.GetNbinsX();
            if (BinY > h_m.GetNbinsY()) BinY = h_m.GetNbinsY();
            fakerate1=h_m->GetBinContent(BinX, BinY);

            BinX = h_m->GetXaxis()->FindBin(fabs(l2_eta));
            BinY = h_m->GetYaxis()->FindBin(l2_pt);
            if (BinX > h_m.GetNbinsX()) BinX = h_m.GetNbinsX();
            if (BinY > h_m.GetNbinsY()) BinY = h_m.GetNbinsY();
            fakerate2=h_m->GetBinContent(BinX, BinY);

            w_temp=fakerate1*fakerate2/((1-fakerate1)*(1-fakerate2));
        }
        return w_temp;
}
