Summary:	Pure PHP Implementation if gettext
Name:		php-gettext-pure
Version:	1.0.7
Release:	0.1
License:	GPL v2
Group:		Development/Languages/PHP
Source0:	http://download.savannah.nongnu.org/releases/php-gettext/php-gettext-%{version}.tar.gz
# Source0-md5:	bc2e032ffe101c78c5be9d174ec593cb
URL:		http://savannah.nongnu.org/projects/php-gettext/
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
%{_datadir}/php/gettext.inc
%{_datadir}/php/gettext.php
%{_datadir}/php/streams.php

%{_examplesdir}/%{name}-%{version}
