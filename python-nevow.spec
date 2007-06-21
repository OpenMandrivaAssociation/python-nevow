Summary: Web application construction kit written in Python
Name: python-nevow
Version: 0.9.18
Release: %mkrel 2
License: MIT
Group: Development/Python
URL: http://divmod.org/trac/wiki/DivmodNevow
# Add ?format=raw to download...
Source: http://divmod.org/trac/attachment/wiki/SoftwareReleases/Nevow-%{version}.tar.gz
Patch:  Nevow-0.9.18-fix_js_installation.diff 
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
%patch -p0

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
