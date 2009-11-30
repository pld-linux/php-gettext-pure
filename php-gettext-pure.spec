Summary:	Pure PHP Implementation if gettext
Summary(pl.UTF-8):	Implementacja gettexta w czystym PHP
Name:		php-gettext-pure
Version:	1.0.8
Release:	1
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://launchpad.net/php-gettext/trunk/%{version}/+download/php-gettext-%{version}.tar.gz
# Source0-md5:	b6c4473329560e095341a7e3d8f96d63
URL:		https://launchpad.net/php-gettext
Requires:	php(mbstring)
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/php,%{_examplesdir}/%{name}-%{version}}
cp -a gettext.inc gettext.php streams.php $RPM_BUILD_ROOT%{_datadir}/php
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%{php_data_dir}/gettext.inc
%{php_data_dir}/gettext.php
%{php_data_dir}/streams.php
%{_examplesdir}/%{name}-%{version}
