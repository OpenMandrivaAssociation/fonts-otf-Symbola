%define fontname	Symbola
%define name		fonts-otf-%{fontname}
%define version		2.53
%define release		%mkrel 3

%define fontdir		%{_datadir}/fonts/OTF/%{fontname}
%define fontconfdir	%{_sysconfdir}/X11/fontpath.d

Summary:	Unicode Symbola fonts
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://users.teilar.gr/~g1951d/%{fontname}253.zip
License:	Public Domain
Group:		System/Fonts/True type
Url:		http://users.teilar.gr/~g1951d/
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

