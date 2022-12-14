# Note that this is NOT a relocatable package
%define ver      3.2.7
%define prefix   /usr
%define enable_gtk_doc 0

%if %{enable_gtk_doc}
%define gtkdoc_configure_flags --enable-gtk-doc
%else
%define gtkdoc_configure_flags --disable-gtk-doc
%endif

Summary: MIME library
Name: gmime
Version: %ver
Release: 1
Copyright: LGPL
Group: Development/Libraries
URL: https://github.com/jstedfast/gmime

Source: ftp://ftp.gnome.org/pub/GNOME/sources/gmime/3.0/gmime-%{version}.tar.bz2
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-root

Requires: glib2 >= 2.26.0
BuildRequires: glib2-devel >= 2.26.0

%description
GMime is a set of utilities for parsing and creating messages using
the Multipurpose Internet Mail Extension (MIME)

%prep
%setup

%build
if [ ! -f configure ]; then
  CFLAGS="$RPM_OPT_FLAGS" ./autogen.sh $ARCHFLAG %{config_opts}
fi
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=${RPM_BUILD_ROOT}

# rename to prevent conflict with uu* utils from sharutils

mv $RPM_BUILD_ROOT%{prefix}/bin/uuencode $RPM_BUILD_ROOT%{prefix}/bin/gmime-uuencode
mv $RPM_BUILD_ROOT%{prefix}/bin/uudecode $RPM_BUILD_ROOT%{prefix}/bin/gmime-uudecode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)

%doc doc/html/* AUTHORS ChangeLog NEWS README LICENSE COPYING TODO
%{prefix}/bin/*
%{prefix}/lib/*.sh
%{prefix}/lib/libgmime*
%{prefix}/lib/pkgconfig/*
%{prefix}/include/gmime-3.0/gmime/*.h
%if %{enable_gtk_doc}
%{_datadir}/gtk-doc/html/*/*
%endif

%changelog
* Mon Nov 29 2004 Ryan Skadberg <skadz@stigmata.org>
- Added in sharp package for .NET bindings

* Wed Dec  9 2002 Benjamin Lee <benjamin.lee@aspectdata.com>
- fixed sharutils conflict with uudecode and uuencode.
- removed duplicate libgmime inclusion in %files.

* Wed Dec  4 2002 Benjamin Lee <benjamin.lee@aspectdata.com>
- fixed files for gtk-doc, pkconfig, and includes.

* Sat Mar 24 2001 Leland Elie <lelie@airmail.net>
- created spec file.
