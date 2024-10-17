%define fontname	Symbola
%define name		fonts-otf-%{fontname}
%define version		2.53
%define release		4

%define fontdir		%{_datadir}/fonts/OTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	Unicode Symbola fonts
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://users.teilar.gr/~g1951d/%{fontname}253.zip
License:	Public Domain
Group:		System/Fonts/True type
Url:		https://users.teilar.gr/~g1951d/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires: fontconfig
BuildRequires:	mkfontscale, mkfontdir

%description
Symbola (formerly issued as Unicode Symbols) covers the following
scripts and symbols supported by The Unicode Standard 5.2:
Basic Latin, Latin-1 Supplement, Latin Extended-A, IPA Extensions,
Spacing Modifier Letters, Greek and Coptic, Cyrillic, Cyrillic
Supplementary, General Punctuation, Superscripts and Subscripts,
Combining Diacritical Marks for Symbols, Letterlike Symbols, Number
Forms, Arrows, Mathematical Operators, Miscellaneous Technical,
Control Pictures, Optical Character Recognition, Box Drawing, Block
Elements, Geometric Shapes, Miscellaneous Symbols, Dingbats,
Miscellaneous Mathematical Symbols-A, Supplemental Arrows-A,
Supplemental Arrows-B, Miscellaneous Mathematical Symbols-B,
Supplemental Mathematical Operators, Miscellaneous Symbols and Arrows,
Supplemental Punctuation, CJK Symbols and Punctuation, Yijing Hexagram
Symbols, Vertical Forms, Combining Half Marks, CJK Compatibility
Forms, Specials, Tai Xuan Jing Symbols, Counting Rod Numerals,
Mathematical Alphanumeric Symbols, Mahjong Tile Symbols, Domino Tile
Symbols.

%prep
%setup -q -c %{name}-%{version}

%install
%__rm -rf %{buildroot}

%__install -m 0755 -d %{buildroot}%{fontdir}
%__install -m 0644 *.otf %{buildroot}%{fontdir}
mkfontscale %{buildroot}%{fontdir}
mkfontdir %{buildroot}%{fontdir}

%__install -m 0755 -d %{buildroot}%{fontconfdir}
ln -s ../../../%{fontdir} %{buildroot}%{fontconfdir}/otf-%{fontname}:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt
%{fontconfdir}/otf*
%{fontdir}/*.otf
%{fontdir}/fonts.*



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 2.53-3mdv2011.0
+ Revision: 675513
- br fontconfig for fc-query used in new rpm-setup-build

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.53-2mdv2011.0
+ Revision: 610724
- rebuild

* Wed Mar 03 2010 Lev Givon <lev@mandriva.org> 2.53-1mdv2010.1
+ Revision: 513935
- import fonts-otf-Symbola

