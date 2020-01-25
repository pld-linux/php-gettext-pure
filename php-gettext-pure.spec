#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		php_min_version 5.0.0
Summary:	Pure PHP Implementation of gettext
Summary(pl.UTF-8):	Implementacja gettexta w czystym PHP
Name:		php-gettext-pure
Version:	1.0.11
Release:	1
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://launchpad.net/php-gettext/trunk/%{version}/+download/php-gettext-%{version}.tar.gz
# Source0-md5:	c085ef92974358adb0faf9350f7973ec
URL:		https://launchpad.net/php-gettext
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
%if %{with tests}
%if %(locale -a | grep -q '^sr_RS$'; echo $?)
# Not provided in PLD Linux by a package
BuildRequires:	locale(sr_SR)
%endif
BuildRequires:	php-PHPUnit
%endif
Requires:	php(core) >= %{php_min_version}
Requires:	php(mbstring)
Requires:	php(pcre)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional php dependencies
%define		_noautophp	php-gettext

# put it together for rpmbuild
%define		_noautoreq	%{?_noautophp} %{?_noautopear}

%description
Provides a simple gettext replacement that works independently from
the system's gettext abilities. It can read MO files and use them for
translating strings. The files are passed to gettext_reader as a
Stream.

This version has the ability to cache all strings and translations to
speed up the string lookup. While the cache is enabled by default, it
can be switched off with the second parameter in the constructor (e.g.
when using very large MO files that you don't want to keep in memory)

%description -l pl.UTF-8
Ten moduł udostępnia prosty zamiennik gettexta działający niezależnie
od systemowych możliwości. Potrafi czytać pliki MO i wykorzystywać je
do tłumaczenia łańcuchów znaków. Pliki te są przekazywane do
gettext_reader jako obiekty Stream.

Ta wersja ma możliwość zapamiętywania (cache'owania) wszystkich
łańcuchów i tłumaczeń w celu przyspieszenia wyszukiwania łańcuchów.
Pamięć podręczna jest domyślnie włączona, ale można ją wyłączyć drugim
parametrem dla konstruktora (np. w przypadku używania bardzo dużych
plików MO, których nie chcemy trzymać w pamięci).

%prep
%setup -q -n php-gettext-%{version}

# make it work for PHPUnit 3.7
%{__sed} -i -e '/PHPUnit\/Framework.php/d' tests/*Test.php

%build
%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/php,%{_examplesdir}/%{name}-%{version}}
cp -a gettext.inc gettext.php streams.php $RPM_BUILD_ROOT%{_datadir}/php
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%{php_data_dir}/gettext.inc
%{php_data_dir}/gettext.php
%{php_data_dir}/streams.php
%{_examplesdir}/%{name}-%{version}
