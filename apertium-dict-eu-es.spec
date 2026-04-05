Summary:	Basque-Spanish language pair for Apertium
Summary(pl.UTF-8):	Para języków baskijski-hiszpański dla Apertium
%define	lpair	eu-es
Name:		apertium-dict-%{lpair}
Version:	0.3.4
Release:	2
License:	GPL v2+
Group:		Applications/Text
Source0:	https://github.com/apertium/apertium-%{lpair}/archive/v%{version}/apertium-%{lpair}-%{version}.tar.gz
# Source0-md5:	36fa999f0606800b78d6a80a5693fda8
URL:		https://www.apertium.org/
BuildRequires:	apertium-devel >= 3.7.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	pkgconfig
Requires:	apertium >= 3.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%undefine	_debugsource_packages

%description
This is an Apertium language pair, which can be used for translating
between Basque and Spanish, morphological analysis or part-of-speech
tagging of both languages.

%description -l pl.UTF-8
Ten pakiet zawiera parę języków dla Apertium służącą do tłumaczenia
między baskijskim a hiszpańskim, a także analizy morfologicznej lub
oznaczania części mowy w obu językach.

%prep
%setup -q -n apertium-%{lpair}-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -j1 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/apertium/apertium-%{lpair}
%{_datadir}/apertium/modes/eu-es.mode
