#
%define	gnome_version	2.25.0
%include	/usr/lib/rpm/macros.mono
%include	/usr/lib/rpm/macros.perl
#
Summary:	.NET language bindings for some of the GNOME desktop libraries
Summary(pl.UTF-8):	Wiązania niektórych bibliotek GNOME desktop dla .NET
Name:		dotnet-gnome-desktop-sharp
Version:	2.26.0
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-desktop-sharp/2.26/gnome-desktop-sharp-%{version}.tar.bz2
# Source0-md5:	4bc990900bb318b2ba0b0e7998bb47d1
URL:		http://gtk-sharp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gnome-sharp-devel >= 2.24.1
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.12.2
BuildRequires:	gnome-desktop-devel >= %{gnome_version}
BuildRequires:	gnome-panel-devel >= %{gnome_version}
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	gtkhtml-devel >= 3.24.0
BuildRequires:	gtksourceview2-devel >= 2.2.2
BuildRequires:	libgnomeprintui-devel >= 2.18.0
BuildRequires:	librsvg-devel >= 2.22.2
BuildRequires:	libtool
BuildRequires:	libwnck-devel >= %{gnome_version}
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	monodoc >= 1.1.16
BuildRequires:	nautilus-cd-burner-devel >= 2.24.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	vte-devel >= 0.16.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides .NET bindings for some of the GNOME desktop
libraries.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania niektórych bibliotek GNOME desktop dla
.NET.

%package devel
Summary:	Development part of GNOMEDesktop#
Summary(pl.UTF-8):	Część dla programistów GNOMEDesktop#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-gnome-sharp-devel >= 2.24.0
Requires:	dotnet-gtk-sharp2-devel >= 2.12.2

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
%{__autoconf}
%{__autoheader}
%{__automake}
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
%attr(755,root,root) %{_libdir}/libgnomepanelsharpglue-2.so
%attr(755,root,root) %{_libdir}/libgtkhtmlsharpglue-2.so
%attr(755,root,root) %{_libdir}/libgtksourceview2sharpglue-2.so
%attr(755,root,root) %{_libdir}/libnautilusburnsharpglue-2.so
%attr(755,root,root) %{_libdir}/libwncksharpglue-2.so
%attr(755,root,root) %{_libdir}/libvtesharpglue-2.so
%{_libdir}/libgnomepanelsharpglue-2.la
%{_libdir}/libgtkhtmlsharpglue-2.la
%{_libdir}/libgtksourceview2sharpglue-2.la
%{_libdir}/libnautilusburnsharpglue-2.la
%{_libdir}/libwncksharpglue-2.la
%{_libdir}/libvtesharpglue-2.la
%{_prefix}/lib/mono/gac/gnome-panel-sharp
%{_prefix}/lib/mono/gac/gnome-print-sharp
%{_prefix}/lib/mono/gac/gnomedesktop-sharp
%{_prefix}/lib/mono/gac/gtkhtml-sharp
%{_prefix}/lib/mono/gac/gtksourceview2-sharp
%{_prefix}/lib/mono/gac/nautilusburn-sharp
%{_prefix}/lib/mono/gac/rsvg2-sharp
%{_prefix}/lib/mono/gac/vte-sharp
%{_prefix}/lib/mono/gac/wnck-sharp

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gnome-panel-sharp-2.24
%{_prefix}/lib/mono/gnome-print-sharp-2.18
%{_prefix}/lib/mono/gnomedesktop-sharp-2.20
%{_prefix}/lib/mono/gtkhtml-sharp-3.14
%{_prefix}/lib/mono/gtksourceview2-sharp-2.0
%{_prefix}/lib/mono/nautilusburn-sharp-2.20
%{_prefix}/lib/mono/rsvg2-sharp-2.0
%{_prefix}/lib/mono/vte-sharp-0.16
%{_prefix}/lib/mono/wnck-sharp-2.20
%{_datadir}/gnome-panel-sharp
%{_datadir}/gnome-print-sharp
%{_datadir}/gnomedesktop-sharp
%{_datadir}/gtkhtml-sharp
%{_datadir}/gtksourceview2-sharp
%{_datadir}/nautilusburn-sharp
%{_datadir}/rsvg2-sharp
%{_datadir}/vte-sharp
%{_datadir}/wnck-sharp
%{_pkgconfigdir}/gnome-desktop-sharp-2.0.pc
%{_pkgconfigdir}/gnome-panel-sharp-2.24.pc
%{_pkgconfigdir}/gnome-print-sharp-2.18.pc
%{_pkgconfigdir}/gtkhtml-sharp-3.14.pc
%{_pkgconfigdir}/gtksourceview2-sharp.pc
%{_pkgconfigdir}/nautilusburn-sharp.pc
%{_pkgconfigdir}/rsvg2-sharp-2.0.pc
%{_pkgconfigdir}/vte-sharp-0.16.pc
%{_pkgconfigdir}/wnck-sharp-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomepanelsharpglue-2.a
%{_libdir}/libgtkhtmlsharpglue-2.a
%{_libdir}/libgtksourceview2sharpglue-2.a
%{_libdir}/libnautilusburnsharpglue-2.a
%{_libdir}/libwncksharpglue-2.a
%{_libdir}/libvtesharpglue-2.a
