%define plugin	bitstreamout

%define debug_package %{nil}

Summary:	VDR plugin: bit stream out to S/P-DIF of a sound card
Name:		vdr-plugin-%plugin
Version:	0.89c
Release:	4
Group:		Video
License:	GPL
URL:		http://bitstreamout.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/bitstreamout/vdr-%plugin-%version.tar.bz2
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	mad-devel
BuildRequires:	libalsa-devel
Requires:	vdr-abi = %vdr_abi
Requires(post):	vdr-common

%description
A plugin which receive the data stream of AC3 (Dolby Digital[tm]),
DTS[tm] (Digital Theater System[tm]), and linear PCM in playback
and live mode of VDR.  The data received is send to the S/P-DIF
of the sound card.  Whereby the none PCM data is embedded into
an appropriate PCM data stream to ensure that the A/V receiver with
its decoder unit is able to handle the data therein.  For a full
description read the file Description.

%prep
%setup -q -c
cd %plugin
# fix build
sed -i 's,error No VDR,warning No VDR,' Makefile

%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# enable a control entry in the main menu
var=ONOFF
param=--onoff
# script for en/dis-able the spdif interface
var=SCRIPT
param=--mute=SCRIPT
%vdr_plugin_params_end

%build
cd %plugin
# messed up variables in Makefile:
%vdr_plugin_build PLUGINLIBDIR=.

%install
cd %plugin
%vdr_plugin_install

install -d -m755 %{buildroot}/%{_mandir}/man5
install -m644 vdr-bitstreamout.5* %{buildroot}/%{_mandir}/man5

%post
%{_bindir}/gpasswd -a vdr audio >/dev/null


%files -f %plugin/%plugin.vdr
%defattr(-,root,root)
%doc %plugin/AUTHORS %plugin/ChangeLog %plugin/Description
%doc %plugin/INSTALL %plugin/PROBLEMS %plugin/README
%doc %plugin/tools %plugin/doc %plugin/mute
%{_mandir}/man5/vdr-bitstreamout.5*



%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.89c-2mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Wed Jul 15 2009 Anssi Hannula <anssi@mandriva.org> 0.89c-1mdv2010.0
+ Revision: 396081
- new version
- make sed in %%prep more specific

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.89b-2mdv2009.1
+ Revision: 359291
- rebuild for new vdr

* Sun May 11 2008 Anssi Hannula <anssi@mandriva.org> 0.89b-1mdv2009.0
+ Revision: 205451
- new version
- drop patches, fixed upstream

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.85-19mdv2009.0
+ Revision: 197904
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.85-18mdv2009.0
+ Revision: 197635
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- fix debug packages (P1 from e-tobi)
- adapt for api changes of vdr 1.5.0 (P2 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.85-17mdv2008.1
+ Revision: 145041
- rebuild for new vdr

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.85-16mdv2008.1
+ Revision: 144991
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.85-15mdv2008.1
+ Revision: 103575
- use own bitops implementation instead of the removed one from
  glibc-devel (replaces P0, from e-tobi)
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.85-14mdv2008.0
+ Revision: 49973
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.85-13mdv2008.0
+ Revision: 42060
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.85-12mdv2008.0
+ Revision: 22713
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.85-11mdv2007.0
+ Revision: 90895
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.85-10mdv2007.1
+ Revision: 73959
- rebuild for new vdr
- Import vdr-plugin-bitstreamout

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.85-9mdv2007.0
- rebuild for new vdr

* Fri Sep 01 2006 Anssi Hannula <anssi@mandriva.org> 0.85-8mdv2007.0
- add vdr to audio group

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.85-7mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.85-6mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.85-5mdv2007.0
- rebuild for new vdr
- patch0: workaround for glibc-devel bug #23935

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.85-4mdv2007.0
- rebuild for new vdr

* Fri Jun 09 2006 Anssi Hannula <anssi@mandriva.org> 0.85-3mdv2007.0
- buildrequires mad-devel libalsa-devel

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 0.85-2mdv2007.0
- rebuild for new vdr

* Sun Jun 04 2006 Anssi Hannula <anssi@mandriva.org> 0.85-1mdv2007.0
- initial Mandriva release

