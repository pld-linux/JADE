Summary:	Java Agent DEvelopment Framework
Name:		jade
Version:	3.2
Release:	0.1
License:	LGPL
Group:		Development/Languages/Java
Source0:	JADE-src-%{version}.zip
# Source0-md5:	3dd2984dd4e61a4eea5f720d854b2f06
URL:		http://jade.tilab.com/
BuildRequires:	jdk
BuildRequires:	jakarta-ant
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
JADE (Java Agent DEvelopment Framework) is a software framework fully
implemented in Java language.

# TODO:
#%package doc
#Summary:	Online manual for jade
#Summary(pl):	Dokumentacja online do jade
#Group:		Documentation

#%description doc

%prep
%setup -q -n %{name}

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
