#
%include	/usr/lib/rpm/macros.mono
%include	/usr/lib/rpm/macros.perl
#
Summary:	.NET language bindings for some of the GNOME desktop libraries
Summary(pl.UTF-8):	Wiązania niektórych bibliotek z GNOME desktop dla .NET
Name:		dotnet-gnome-desktop-sharp
Version:	2.20.1
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-desktop-sharp/2.20/gnome-desktop-sharp-%{version}.tar.bz2
# Source0-md5:	874cfcf8a6547476906b638355a0ed2f
URL:		http://gtk-sharp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gnome-sharp-devel >= 2.20.0
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.12.0
BuildRequires:	gtkhtml-devel >= 3.16.0
BuildRequires:	gtksourceview2-devel >= 2.0.0
BuildRequires:	librsvg-devel >= 2.18.2
BuildRequires:	libtool
BuildRequires:	libwnck-devel > 2.20.0
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	monodoc >= 1.1.16
BuildRequires:	nautilus-cd-burner-devel >= 2.20.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	vte-devel >= 0.16.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides .NET bindings for some of the GNOME desktop libraries.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania niektórych bibliotek z GNOME desktop dla .NET.

%package devel
Summary:	Development part of GNOMEDesktop#
Summary(pl.UTF-8):	Część dla programistów GNOMEDesktop#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Tools (C source parser and C# code generator) and documentation for
developing applications using GNOMEDesktop#.

%description devel -l pl.UTF-8
Narzędzia (parser kodu C oraz generator kodu C#) i dokumentacja
potrzebne przy tworzeniu aplikacji korzystających z GNOMEDesktop#.

%package static
Summary:	Static GNOMEDesktop# libraries
Summary(pl.UTF-8):	Biblioteki statyczne GNOMEDesktop#
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GNOMEDesktop# libraries.

%description static -l pl.UTF-8
Biblioteki statyczne GNOMEDesktop#.

%prep
%setup -q -n gnome-desktop-sharp-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	monodocdir=%{_libdir}/monodoc/sources

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvtesharpglue-2.so
%{_libdir}/libvtesharpglue-2.la
%{_prefix}/lib/mono/gac/gnomedesktop-sharp
%{_prefix}/lib/mono/gac/gtkhtml-sharp
%{_prefix}/lib/mono/gac/gtksourceview2-sharp
%{_prefix}/lib/mono/gac/nautilusburn-sharp
%{_prefix}/lib/mono/gac/rsvg2-sharp
%{_prefix}/lib/mono/gac/vte-sharp
%{_prefix}/lib/mono/gac/wnck-sharp

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/gnome-desktop-sharp-2.0.pc
%{_pkgconfigdir}/gtkhtml-sharp-3.14.pc
%{_pkgconfigdir}/gtksourceview2-sharp.pc
%{_pkgconfigdir}/nautilusburn-sharp.pc
%{_pkgconfigdir}/rsvg2-sharp-2.0.pc
%{_pkgconfigdir}/vte-sharp-0.16.pc
%{_pkgconfigdir}/wnck-sharp-1.0.pc

%{_datadir}/gnomedesktop-sharp
%{_datadir}/gtkhtml-sharp
%{_datadir}/gtksourceview2-sharp
%{_datadir}/nautilusburn-sharp
%{_datadir}/rsvg2-sharp
%{_datadir}/vte-sharp
%{_datadir}/wnck-sharp
%{_prefix}/lib/mono/gnomedesktop-sharp-2.20
%{_prefix}/lib/mono/gtkhtml-sharp-3.14
%{_prefix}/lib/mono/gtksourceview2-sharp-2.0
%{_prefix}/lib/mono/nautilusburn-sharp-2.20
%{_prefix}/lib/mono/rsvg2-sharp-2.0
%{_prefix}/lib/mono/vte-sharp-0.16
%{_prefix}/lib/mono/wnck-sharp-2.20

%files static
%defattr(644,root,root,755)
%{_libdir}/libvtesharpglue-2.a
