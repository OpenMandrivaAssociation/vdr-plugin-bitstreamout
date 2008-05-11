
%define plugin	bitstreamout
%define name	vdr-plugin-%plugin
%define version	0.89b
%define rel	1

Summary:	VDR plugin: bit stream out to S/P-DIF of a sound card
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://bitstreamout.sourceforge.net/
Source:		http://prdownloads.sourceforge.net/bitstreamout/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
sed -i 's,error No,warning No,' Makefile

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
rm -rf %{buildroot}
cd %plugin
%vdr_plugin_install

install -d -m755 %{buildroot}/%{_mandir}/man5
install -m644 vdr-bitstreamout.5* %{buildroot}/%{_mandir}/man5

%clean
rm -rf %{buildroot}

%post
%{_bindir}/gpasswd -a vdr audio >/dev/null
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin/%plugin.vdr
%defattr(-,root,root)
%doc %plugin/AUTHORS %plugin/ChangeLog %plugin/Description
%doc %plugin/INSTALL %plugin/PROBLEMS %plugin/README
%doc %plugin/tools %plugin/doc %plugin/mute
%{_mandir}/man5/vdr-bitstreamout.5*

