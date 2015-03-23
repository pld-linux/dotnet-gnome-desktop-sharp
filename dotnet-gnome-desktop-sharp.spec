#
# Conditional build:
%bcond_with	nautilusburn	# NautilusBurn# binding
%bcond_with	gnomepanel	# GnomePanel# binding

%define	gnome_ver		2.25.0
%define	gnomesharp_ver		2.24.1
%define	gtkhtml_ver		3.23.5
%define	gtksharp_ver		2.12.2
%define	gtksourceview_ver	2.2.2
%define	libgnomeprint_ver	2.18.0
%define	librsvg_ver		2.22.2
%define	nautilusburn_ver	2.22.1
%define	vte_ver			0.16.14

%include	/usr/lib/rpm/macros.mono
%include	/usr/lib/rpm/macros.perl
Summary:	GnomeDesktop# - .NET binding for GNOME Desktop library
Summary(pl.UTF-8):	GnomeDesktop# - wiązanie .NET do biblioteki GNOME Desktop
Name:		dotnet-gnome-desktop-sharp
Version:	2.26.0
Release:	7
License:	LGPL v2.1
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-desktop-sharp/2.26/gnome-desktop-sharp-%{version}.tar.bz2
# Source0-md5:	4bc990900bb318b2ba0b0e7998bb47d1
Patch0:		gnome-desktop-soname.patch
Patch1:		%{name}-opt.patch
URL:		http://gtk-sharp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gnome-sharp-devel >= %{gnomesharp_ver}
BuildRequires:	dotnet-gtk-sharp2-devel >= %{gtksharp_ver}
BuildRequires:	gnome-desktop2-devel >= %{gnome_ver}
%if %{with gnomepanel}
BuildRequires:	gnome-panel-devel >= %{gnome_ver}
BuildRequires:	gnome-panel-devel < 3
%endif
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	gtkhtml3-devel >= %{gtkhtml_ver}
BuildRequires:	gtksourceview2-devel >= %{gtksourceview_ver}
BuildRequires:	libgnomeprintui-devel >= %{libgnomeprint_ver}
BuildRequires:	librsvg-devel >= %{librsvg_ver}
BuildRequires:	libtool
BuildRequires:	libwnck2-devel >= %{gnome_ver}
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	monodoc >= 1.1.16
%{?with_nautilusburn:BuildRequires:	nautilus-cd-burner-devel >= %{nautilusburn_ver}}
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov
BuildRequires:	rpmbuild(monoautodeps)
BuildRequires:	vte0-devel >= %{vte_ver}
%{!?with_nautilusburn:BuildConflicts:	nautilus-cd-burner-devel}
Requires:	gnome-desktop2 >= 2.30
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides .NET bindings for some of the GNOME desktop
libraries.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania niektórych bibliotek GNOME desktop dla
.NET.

%package devel
Summary:	Development files for GnomeDesktop# library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GnomeDesktop#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-gnome-sharp-devel >= %{gnomesharp_ver}
Requires:	dotnet-gtk-sharp2-devel >= %{gtksharp_ver}

%description devel
Development files for GnomeDesktop# library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki GnomeDesktop#.

%package static
Summary:	Static GNOMEDesktop# libraries
Summary(pl.UTF-8):	Biblioteki statyczne GNOMEDesktop#
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GNOMEDesktop# libraries.

%description static -l pl.UTF-8
Biblioteki statyczne GNOMEDesktop#.

%package -n dotnet-gnome-panel-sharp
Summary:	GnomePanel# - .NET binding for libpanelapplet library
Summary(pl.UTF-8):	GnomePanel# - wiązanie .NET do biblioteki libpanelapplet
Group:		Libraries
Requires:	dotnet-gtk-sharp2 >= %{gtksharp_ver}
Requires:	gnome-panel-devel >= %{gnome_ver}
Conflicts:	dotnet-gnome-desktop-sharp < 2.26.0-7

%description -n dotnet-gnome-panel-sharp
GnomePanel# - .NET binding for libpanelapplet library.

%description -n dotnet-gnome-panel-sharp -l pl.UTF-8
GnomePanel# - wiązanie .NET do biblioteki libpanelapplet.

%package -n dotnet-gnome-panel-sharp-devel
Summary:	Development files for GnomePanel# library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GnomePanel#
Group:		Development/Libraries
Requires:	dotnet-gnome-panel-sharp = %{version}-%{release}
Requires:	dotnet-gtk-sharp2-devel >= %{gtksharp_ver}

%description -n dotnet-gnome-panel-sharp-devel
Development files for GnomePanel# library.

%description -n dotnet-gnome-panel-sharp-devel -l pl.UTF-8
Pliki programistyczne biblioteki GnomePanel#.

%package -n dotnet-gnome-panel-sharp-static
Summary:	Static GnomePanel# glue library
Summary(pl.UTF-8):	Statyczna biblioteka sklejająca GnomePanel#
Group:		Development/Libraries
Requires:	dotnet-gnome-panel-sharp-devel = %{version}-%{release}
Obsoletes:	dotnet-gnome-desktop-sharp-static

%description -n dotnet-gnome-panel-sharp-static
Static GnomePanel# glue library.

%description -n dotnet-gnome-panel-sharp-static -l pl.UTF-8
Statyczna biblioteka sklejająca GnomePanel#.

%package -n dotnet-gnome-print-sharp
Summary:	GnomePrint# - .NET binding for libgnomeprint libraries
Summary(pl.UTF-8):	GnomePrint# - wiązanie .NET do bibliotek libgnomeprint
Group:		Libraries
Requires:	dotnet-gtk-sharp2 >= %{gtksharp_ver}
Requires:	libgnomeprintui >= %{libgnomeprint_ver}
Conflicts:	dotnet-gnome-desktop-sharp < 2.26.0-7

%description -n dotnet-gnome-print-sharp
GnomePrint# - .NET binding for libgnomeprint and libgnomeprintui
libraries.

%description -n dotnet-gnome-print-sharp -l pl.UTF-8
GnomePrint# - wiązanie .NET do bibliotek libgnomeprint oraz
libgnomeprintui.

%package -n dotnet-gnome-print-sharp-devel
Summary:	Development files for GnomePrint# library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GnomePrint#
Group:		Development/Libraries
Requires:	dotnet-gnome-print-sharp = %{version}-%{release}
Requires:	dotnet-gtk-sharp2-devel >= %{gtksharp_ver}

%description -n dotnet-gnome-print-sharp-devel
Development files for GnomePrint# library.

%description -n dotnet-gnome-print-sharp-devel -l pl.UTF-8
Pliki programistyczne biblioteki GnomePrint#.

%package -n dotnet-gtkhtml-sharp
Summary:	Gtkhtml# - .NET binding for Gtkhtml library
Summary(pl.UTF-8):	Gtkhtml# - wiązanie .NET do biblioteki Gtkhtml
Group:		Libraries
Requires:	dotnet-gtk-sharp2 >= %{gtksharp_ver}
Requires:	gtkhtml3-devel >= %{gtkhtml_ver}
Conflicts:	dotnet-gnome-desktop-sharp < 2.26.0-7

%description -n dotnet-gtkhtml-sharp
Gtkhtml# - .NET binding for Gtkhtml library.

%description -n dotnet-gtkhtml-sharp -l pl.UTF-8
Gtkhtml# - wiązanie .NET do biblioteki Gtkhtml.

%package -n dotnet-gtkhtml-sharp-devel
Summary:	Development files for Gtkhtml# library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Gtkhtml#
Group:		Development/Libraries
Requires:	dotnet-gtk-sharp2-devel >= %{gtksharp_ver}
Requires:	dotnet-gtkhtml-sharp = %{version}-%{release}

%description -n dotnet-gtkhtml-sharp-devel
Development files for Gtkhtml# library.

%description -n dotnet-gtkhtml-sharp-devel -l pl.UTF-8
Pliki programistyczne biblioteki Gtkhtml#.

%package -n dotnet-gtkhtml-sharp-static
Summary:	Static Gtkhtml# glue library
Summary(pl.UTF-8):	Statyczna biblioteka sklejająca Gtkhtml#
Group:		Development/Libraries
Requires:	dotnet-gtkhtml-sharp-devel = %{version}-%{release}
Obsoletes:	dotnet-gnome-desktop-sharp-static

%description -n dotnet-gtkhtml-sharp-static
Static Gtkhtml# glue library.

%description -n dotnet-gtkhtml-sharp-static -l pl.UTF-8
Statyczna biblioteka sklejająca Gtkhtml#.

%package -n dotnet-gtksourceview2-sharp
Summary:	GtkSourceView# - .NET binding for gtksourceview library
Summary(pl.UTF-8):	GtkSourceView# - wiązanie .NET do biblioteki gtksourceview
Group:		Libraries
Requires:	dotnet-gtk-sharp2 >= %{gtksharp_ver}
Requires:	gtksourceview2 >= %{gtksourceview_ver}
Conflicts:	dotnet-gnome-desktop-sharp < 2.26.0-7

%description -n dotnet-gtksourceview2-sharp
GtkSourceView# - .NET binding for gtksourceview library.

%description -n dotnet-gtksourceview2-sharp -l pl.UTF-8
GtkSourceView# - wiązanie .NET do biblioteki gtksourceview.

%package -n dotnet-gtksourceview2-sharp-devel
Summary:	Development files for GtkSourceView# library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki GtkSourceView#
Group:		Development/Libraries
Requires:	dotnet-gtk-sharp2-devel >= %{gtksharp_ver}
Requires:	dotnet-gtksourceview2-sharp = %{version}-%{release}

%description -n dotnet-gtksourceview2-sharp-devel
Development files for GtkSourceView# library.

%description -n dotnet-gtksourceview2-sharp-devel -l pl.UTF-8
Pliki programistyczne biblioteki GtkSourceView#.

%package -n dotnet-gtksourceview2-sharp-static
Summary:	Static GtkSourceView# glue library
Summary(pl.UTF-8):	Statyczna biblioteka sklejająca GtkSourceView#
Group:		Development/Libraries
Requires:	dotnet-gtksourceview2-sharp-devel = %{version}-%{release}
Obsoletes:	dotnet-gnome-desktop-sharp-static

%description -n dotnet-gtksourceview2-sharp-static
Static GtkSourceView# glue library.

%description -n dotnet-gtksourceview2-sharp-static -l pl.UTF-8
Statyczna biblioteka sklejająca GtkSourceView#.

%package -n dotnet-nautilusburn-sharp
Summary:	NautilusBurn# - .NET binding for libnautilus-burn library
Summary(pl.UTF-8):	NautilusBurn# - wiązanie .NET do biblioteki libnautilus-burn
Group:		Libraries
Requires:	nautilus-cd-burner-libs >= %{nautilusburn_ver}
Conflicts:	dotnet-gnome-desktop-sharp < 2.26.0-7

%description -n dotnet-nautilusburn-sharp
NautilusBurn# - .NET binding for libnautilus-burn library.

%description -n dotnet-nautilusburn-sharp -l pl.UTF-8
NautilusBurn# - wiązanie .NET do biblioteki libnautilus-burn.

%package -n dotnet-nautilusburn-sharp-devel
Summary:	Development files for NautilusBurn# library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki NautilusBurn#
Group:		Development/Libraries
Requires:	dotnet-nautilusburn-sharp = %{version}-%{release}

%description -n dotnet-nautilusburn-sharp-devel
Development files for NautilusBurn# library.

%description -n dotnet-nautilusburn-sharp-devel -l pl.UTF-8
Pliki programistyczne biblioteki NautilusBurn#.

%package -n dotnet-nautilusburn-sharp-static
Summary:	Static NautilusBurn# glue library
Summary(pl.UTF-8):	Statyczna biblioteka sklejająca NautilusBurn#
Group:		Development/Libraries
Requires:	dotnet-nautilusburn-sharp-devel = %{version}-%{release}
Obsoletes:	dotnet-gnome-desktop-sharp-static

%description -n dotnet-nautilusburn-sharp-static
Static NautilusBurn# glue library.

%description -n dotnet-nautilusburn-sharp-static -l pl.UTF-8
Statyczna biblioteka sklejająca NautilusBurn#.

%package -n dotnet-rsvg2-sharp
Summary:	Rsvg# - .NET binding for librsvg library
Summary(pl.UTF-8):	Rsvg# - wiązanie .NET do biblioteki librsvg
Group:		Libraries
Requires:	librsvg >= %{librsvg_ver}
Conflicts:	dotnet-gnome-desktop-sharp < 2.26.0-7

%description -n dotnet-rsvg2-sharp
Rsvg# - .NET binding for librsvg library.

%description -n dotnet-rsvg2-sharp -l pl.UTF-8
Rsvg# - wiązanie .NET do biblioteki librsvg.

%package -n dotnet-rsvg2-sharp-devel
Summary:	Development files for Rsvg# library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Rsvg#
Group:		Development/Libraries
Requires:	dotnet-rsvg2-sharp = %{version}-%{release}

%description -n dotnet-rsvg2-sharp-devel
Development files for Rsvg# library.

%description -n dotnet-rsvg2-sharp-devel -l pl.UTF-8
Pliki programistyczne biblioteki Rsvg#.

%package -n dotnet-vte-sharp
Summary:	Vte# - .NET binding for libvte library
Summary(pl.UTF-8):	Vte# - wiązanie .NET do biblioteki libvte
Group:		Libraries
Requires:	dotnet-gtk-sharp2 >= %{gtksharp_ver}
Requires:	vte0 >= %{vte_ver}
Conflicts:	dotnet-gnome-desktop-sharp < 2.26.0-7

%description -n dotnet-vte-sharp
Vte# - .NET binding for libvte library.

%description -n dotnet-vte-sharp -l pl.UTF-8
Vte# - wiązanie .NET do biblioteki libvte.

%package -n dotnet-vte-sharp-devel
Summary:	Development files for Vte# library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Vte#
Group:		Development/Libraries
Requires:	dotnet-gtk-sharp2-devel >= %{gtksharp_ver}
Requires:	dotnet-vte-sharp = %{version}-%{release}

%description -n dotnet-vte-sharp-devel
Development files for Vte# library.

%description -n dotnet-vte-sharp-devel -l pl.UTF-8
Pliki programistyczne biblioteki Vte#.

%package -n dotnet-vte-sharp-static
Summary:	Static Vte# glue library
Summary(pl.UTF-8):	Statyczna biblioteka sklejająca Vte#
Group:		Development/Libraries
Requires:	dotnet-vte-sharp-devel = %{version}-%{release}
Obsoletes:	dotnet-gnome-desktop-sharp-static

%description -n dotnet-vte-sharp-static
Static Vte# glue library.

%description -n dotnet-vte-sharp-static -l pl.UTF-8
Statyczna biblioteka sklejająca Vte#.

%package -n dotnet-wnck-sharp
Summary:	Wnck# - .NET binding for libwnck library
Summary(pl.UTF-8):	Wnck# - wiązanie .NET do biblioteki libwnck
Group:		Libraries
Requires:	dotnet-gtk-sharp2 >= %{gtksharp_ver}
Requires:	libwnck2 >= %{gnome_ver}
Conflicts:	dotnet-gnome-desktop-sharp < 2.26.0-7

%description -n dotnet-wnck-sharp
Wnck# - .NET binding for libwnck library.

%description -n dotnet-wnck-sharp -l pl.UTF-8
Wnck# - wiązanie .NET do biblioteki libwnck.

%package -n dotnet-wnck-sharp-devel
Summary:	Development files for Wnck# library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki Wnck#
Group:		Development/Libraries
Requires:	dotnet-gtk-sharp2-devel >= %{gtksharp_ver}
Requires:	dotnet-wnck-sharp = %{version}-%{release}

%description -n dotnet-wnck-sharp-devel
Development files for Wnck# library.

%description -n dotnet-wnck-sharp-devel -l pl.UTF-8
Pliki programistyczne biblioteki Wnck#.

%package -n dotnet-wnck-sharp-static
Summary:	Static Wnck# glue library
Summary(pl.UTF-8):	Statyczna biblioteka sklejająca Wnck#
Group:		Development/Libraries
Requires:	dotnet-wnck-sharp-devel = %{version}-%{release}
Obsoletes:	dotnet-gnome-desktop-sharp-static

%description -n dotnet-wnck-sharp-static
Static Wnck# glue library.

%description -n dotnet-wnck-sharp-static -l pl.UTF-8
Statyczna biblioteka sklejająca Wnck#.

%prep
%setup -q -n gnome-desktop-sharp-%{version}
%patch0 -p1
%patch1 -p1

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

%post	-n dotnet-gnome-panel-sharp -p /sbin/ldconfig
%postun	-n dotnet-gnome-panel-sharp -p /sbin/ldconfig

%post	-n dotnet-gtkhtml-sharp -p /sbin/ldconfig
%postun	-n dotnet-gtkhtml-sharp -p /sbin/ldconfig

%post	-n dotnet-gtksourceview2-sharp -p /sbin/ldconfig
%postun	-n dotnet-gtksourceview2-sharp -p /sbin/ldconfig

%post	-n dotnet-nautilusburn-sharp -p /sbin/ldconfig
%postun	-n dotnet-nautilusburn-sharp -p /sbin/ldconfig

%post	-n dotnet-vte-sharp -p /sbin/ldconfig
%postun	-n dotnet-vte-sharp -p /sbin/ldconfig

%post	-n dotnet-wnck-sharp -p /sbin/ldconfig
%postun	-n dotnet-wnck-sharp -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_prefix}/lib/mono/gac/gnomedesktop-sharp

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gnomedesktop-sharp-2.20
%{_datadir}/gnomedesktop-sharp
%{_pkgconfigdir}/gnome-desktop-sharp-2.0.pc

%if %{with gnomepanel}
%files -n dotnet-gnome-panel-sharp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomepanelsharpglue-2.so
%{_libdir}/libgnomepanelsharpglue-2.la
%{_prefix}/lib/mono/gac/gnome-panel-sharp

%files -n dotnet-gnome-panel-sharp-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gnome-panel-sharp-2.24
%{_pkgconfigdir}/gnome-panel-sharp-2.24.pc

%files -n dotnet-gnome-panel-sharp-static
%defattr(644,root,root,755)
%{_libdir}/libgnomepanelsharpglue-2.a
%endif

%files -n dotnet-gnome-print-sharp
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/gnome-print-sharp

%files -n dotnet-gnome-print-sharp-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gnome-print-sharp-2.18
%{_datadir}/gnome-print-sharp
%{_pkgconfigdir}/gnome-print-sharp-2.18.pc

%files -n dotnet-gtkhtml-sharp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtkhtmlsharpglue-2.so
%{_libdir}/libgtkhtmlsharpglue-2.la
%{_prefix}/lib/mono/gac/gtkhtml-sharp

%files -n dotnet-gtkhtml-sharp-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtkhtml-sharp-3.14
%{_datadir}/gtkhtml-sharp
%{_pkgconfigdir}/gtkhtml-sharp-3.14.pc

%files -n dotnet-gtkhtml-sharp-static
%defattr(644,root,root,755)
%{_libdir}/libgtkhtmlsharpglue-2.a

%files -n dotnet-gtksourceview2-sharp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgtksourceview2sharpglue-2.so
%{_libdir}/libgtksourceview2sharpglue-2.la
%{_prefix}/lib/mono/gac/gtksourceview2-sharp

%files -n dotnet-gtksourceview2-sharp-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gtksourceview2-sharp-2.0
%{_datadir}/gtksourceview2-sharp
%{_pkgconfigdir}/gtksourceview2-sharp.pc

%files -n dotnet-gtksourceview2-sharp-static
%defattr(644,root,root,755)
%{_libdir}/libgtksourceview2sharpglue-2.a

%if %{with nautilusburn}
%files -n dotnet-nautilusburn-sharp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnautilusburnsharpglue-2.so
%{_libdir}/libnautilusburnsharpglue-2.la
%{_prefix}/lib/mono/gac/nautilusburn-sharp

%files -n dotnet-nautilusburn-sharp-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/nautilusburn-sharp
%{_datadir}/nautilusburn-sharp
%{_pkgconfigdir}/nautilusburn-sharp.pc

%files -n dotnet-nautilusburn-sharp-static
%defattr(644,root,root,755)
%{_libdir}/libnautilusburnsharpglue-2.a
%endif

%files -n dotnet-rsvg2-sharp
%defattr(644,root,root,755)
%{_prefix}/lib/mono/gac/rsvg2-sharp

%files -n dotnet-rsvg2-sharp-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/rsvg2-sharp-2.0
%{_datadir}/rsvg2-sharp
%{_pkgconfigdir}/rsvg2-sharp-2.0.pc

%files -n dotnet-vte-sharp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvtesharpglue-2.so
%{_libdir}/libvtesharpglue-2.la
%{_prefix}/lib/mono/gac/vte-sharp

%files -n dotnet-vte-sharp-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/vte-sharp-0.16
%{_datadir}/vte-sharp
%{_pkgconfigdir}/vte-sharp-0.16.pc

%files -n dotnet-vte-sharp-static
%defattr(644,root,root,755)
%{_libdir}/libvtesharpglue-2.a

%files -n dotnet-wnck-sharp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwncksharpglue-2.so
%{_libdir}/libwncksharpglue-2.la
%{_prefix}/lib/mono/gac/wnck-sharp

%files -n dotnet-wnck-sharp-devel
%defattr(644,root,root,755)
%{_prefix}/lib/mono/wnck-sharp-2.20
%{_datadir}/wnck-sharp
%{_pkgconfigdir}/wnck-sharp-1.0.pc

%files -n dotnet-wnck-sharp-static
%defattr(644,root,root,755)
%{_libdir}/libwncksharpglue-2.a
