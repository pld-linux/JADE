Summary:	Java Agent DEvelopment Framework
Summary(pl):	Szkielet do programowania w Javie
Name:		JADE
Version:	3.2
Release:	0.1
License:	LGPL
Group:		Development/Languages/Java
# http://jade.tilab.com/download.php - download requires registration?!
Source0:	%{name}-src-%{version}.zip
# Source0-md5:	3dd2984dd4e61a4eea5f720d854b2f06
URL:		http://jade.tilab.com/
BuildRequires:	jakarta-ant
BuildRequires:	jdk
BuildRequires:  unzip
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JADE (Java Agent DEvelopment Framework) is a software framework fully
implemented in Java language.

%description -l pl
JADE (Java Agent DEvelopment Framework) to szkielet oprogramowania w
pe³ni zaimplementowany w jêzyku Java.

# TODO:
#%package doc
#Summary:	Online manual for JADE
#Summary(pl):	Dokumentacja online do JADE
#Group:		Documentation

#%description doc

%prep
%setup -q -n jade

%build
ant jade
ant lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_javadir}/%{name}}

install lib/*.jar $RPM_BUILD_ROOT%{_javadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%{_javadir}/%{name}

#%files doc
#%defattr(644,root,root,755)
#%doc docs
