Summary:	Jade -- DSSSL parser
Summary(pl):	Jade -- parser DSSSL
Name:		jade
%define		jver  1.2.1
%define		spver 1.3.3
Version:	%{jver}
Release:	6
Serial:		7
Vendor:		James Clark
Group:		Applications/Publishing/SGML
Group(pl):	Aplikacje/Publikowanie/SGML
Copyright:	(C) 1997 James Clark (free)
Source0:	ftp://ftp.jclark.com/pub/jade/%{name}-%{version}.tar.gz
Source1:	unicode.cat
Source2:	dsssl.cat
Source3:	sp-html.cat
Patch0:		jade-DESTDIR.patch
Patch1:		jade-manpages.patch
Patch2:		jade-c++_fix.patch
Provides:	dssslparser
URL:		http://www.jclark.com/jade/
Prereq:		%{_sbindir}/install-catalog
Requires:	sgml-common
Requires:	sp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jade (James' DSSSL Engine) is an implementation of the DSSSL style language. 

%description -l pl
Jade (James' DSSSL Engine) jest implementacj± parsera DSSSL.

%package -n sp
Summary:	SP -- parser and tools for SGML
Summary(pl):	SP -- parser and tools for SGML
Group:		Applications/Publishing/SGML
Group(pl):	Aplikacje/Publikowanie/SGML
Version:	%{spver}
URL:		http://www.jclark.com/sp/
Prereq:		/usr/sbin/install-catalog
Provides:	sgmlparser
Requires:	sgml-common

%description -n sp
SGML parser called sp (replacement of sgmls).

%description -n sp -l pl
Parser SGML (bêd±cy nastêpc± pisanego w C sgmls) oraz narzêdzia
do normalizacji SGML-a (sgmlnorm), konwersji tego¿ do XMLa (sx).

%prep
%setup  -q  
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f configure
mv config/configure.in .
autoconf -l config
libtoolize --copy --force
LDFLAGS="-s"
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-implicit-templates -fpermissive"
export CXXFLAGS LDFLAGS
%configure \
	--sharedstatedir=%{_datadir} \
	--enable-default-catalog=%{_datadir}/sgml/CATALOG  \
	--enable-shared \
	--enable-http \
	--with-gnu-ld \
	--enable-mif

%{__make}  

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_datadir}/sgml/{dsssl/jade,html}}

%{__make} install DESTDIR="$RPM_BUILD_ROOT"

cp -ar pubtext/* $RPM_BUILD_ROOT%{_datadir}/sgml/html
cp -ar unicode $RPM_BUILD_ROOT%{_datadir}/sgml

install $RPM_SOURCE_DIR/{dsssl,sp-html,unicode}.cat \
	$RPM_BUILD_ROOT/usr/share/sgml

cp -ar dsssl/catalog $RPM_BUILD_ROOT%{_datadir}/sgml/dsssl/jade
cp -ar dsssl/dsssl.dtd dsssl/style-sheet.dtd dsssl/fot.dtd \
	$RPM_BUILD_ROOT%{_datadir}/sgml/dsssl/jade

install */*.1 $RPM_BUILD_ROOT%{_mandir}/man1

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README COPYING

%post
%{_sbindir}/install-catalog --install dsssl --version %{jver}-%{release}
/sbin/ldconfig

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/install-catalog --remove dsssl --version %{jver}-%{release}
fi

%postun -p /sbin/ldconfig

%post -n sp
%{_sbindir}/install-catalog --install sp-html --version %{spver}-%{release}
%{_sbindir}/install-catalog --install unicode --version %{spver}-%{release}
/sbin/ldconfig

%preun -n sp
if [ "$1" = "0" ]; then
	%{_sbindir}/install-catalog --remove sp-html --version %{spver}-%{release} 
	%{_sbindir}/install-catalog --remove unicode --version %{spver}-%{release}
fi

%postun -n sp -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc jadedoc/ dsssl/ *gz

%attr(755,root,root) %{_bindir}/jade
%attr(755,root,root) %{_libdir}/libstyle.so.*.*
%attr(755,root,root) %{_libdir}/libgrove.so.*.*
%attr(755,root,root) %{_libdir}/libspgrove.so.*.*

%{_datadir}/sgml/dsssl.cat
%{_datadir}/sgml/dsssl/*

%files -n sp
%defattr(644,root,root,755)
%doc doc/*.htm

%attr(755,root,root) %{_bindir}/s*
%attr(755,root,root) %{_bindir}/nsgmls
%attr(755,root,root) %{_libdir}/libsp.so.*.*

%{_datadir}/sgml/sp-html.cat
%{_datadir}/sgml/html

%{_datadir}/sgml/unicode.cat
%{_datadir}/sgml/unicode

%{_mandir}/man1/spam.1*
%{_mandir}/man1/spent.1*
%{_mandir}/man1/nsgmls.1*
