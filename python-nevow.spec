Summary: Web application construction kit written in Python
Name: python-nevow
Version: 0.9.32
Release: 3
License: MIT
Group: Development/Python
URL: http://divmod.org/trac/wiki/DivmodNevow
# Add ?format=raw to download...
Source: http://divmod.org/trac/attachment/wiki/SoftwareReleases/Nevow-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: python-twisted-core
Requires: python-twisted-web
BuildRequires: python-devel
BuildRequires: python-twisted-core
BuildRequires: python-twisted-web
# To fix up docs
Buildrequires: dos2unix
BuildArch:     noarch
%description
Nevow (pronounced as the French "nouveau", or "noo-voh") is a web application
construction kit written in Python. It is designed to allow the programmer to
express as much of the view logic as desired in Python.


%prep
%setup -q -n Nevow-%{version}
# Convert all DOS files to UNIX
find examples \( -name '*.html' -o -name '*.xml' -o -name '*.css' \) \
    -exec dos2unix {} \;
# Remove +x from executable doc files
%{__chmod} -x examples/i18n/update-l10n examples/wsgi/test-cgi.py

%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install --skip-build --root %{buildroot} --install-purelib=%{py_puresitedir}
# Install man page
%{__install} -D -p -m 0644 doc/man/nevow-xmlgettext.1 \
    %{buildroot}%{_mandir}/man1/nevow-xmlgettext.1


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc ChangeLog LICENSE README doc/txt/* examples/
%{_bindir}/nevow-xmlgettext
%{_bindir}/nit
%{py_puresitedir}/formless/
%{py_puresitedir}/nevow/
%{_mandir}/man1/nevow-xmlgettext.1*
%{py_puresitedir}/Nevow-%{version}*.egg-info
%{py_puresitedir}/twisted/plugins/


%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.9.32-2mdv2010.0
+ Revision: 442321
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.9.32-1mdv2009.1
+ Revision: 323812
- new version 0.9.32

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 0.9.31-1mdv2009.0
+ Revision: 280481
- New release

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.9.18-5mdv2009.0
+ Revision: 259737
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.9.18-4mdv2009.0
+ Revision: 247521
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.9.18-2mdv2008.1
+ Revision: 136452
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jun 21 2007 Thierry Vignaud <tv@mandriva.org> 0.9.18-2mdv2008.0
+ Revision: 42303
- fix group

* Sat Jun 16 2007 Michael Scherer <misc@mandriva.org> 0.9.18-1mdv2008.0
+ Revision: 40430
- fix installation of various js file
- mark package as noarch and fix build on x86_64

  + Jérôme Soyer <saispo@mandriva.org>
    - Import python-nevow

