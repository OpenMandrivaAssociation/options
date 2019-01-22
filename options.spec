%{?_javapackages_macros:%_javapackages_macros}

Name:           options
Version:        1.4
Release:        5.2
Summary:        Library for managing sets of JVM properties to configure an app or library
Group:		Development/Java
License:        ASL 2.0
URL:            https://github.com/headius/%{name}
Source0:        https://github.com/headius/%{name}/archive/%{name}-%{version}.zip
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch
BuildRequires:  maven-local

%description
Provides a simple mechanism for defining JVM property-based
configuration for an application or library.

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE1} .

%build
%mvn_build

%install
%mvn_install

%files  -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE-2.0.txt

%changelog
* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Dec 05 2014 Mo Morsi <mmorsi@redhat.com> - 1.2-4
- Remove Group from javadoc package, add license to
  both packages

* Wed Dec 03 2014 Mo Morsi <mmorsi@redhat.com> - 1.2-3
- Moved LICENSE-2.0.txt file to main pkg, marked as doc

* Tue Oct 14 2014 Mo Morsi <mmorsi@redhat.com> - 1.2-2
- Include license text, remove group tag
- Update to comply with Fedora guidelines

* Mon Oct 13 2014 Mo Morsi <mmorsi@redhat.com> - 1.2-1
- Initial package
