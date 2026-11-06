Name:		options
Version:	1.7
Release:	1
Summary:	JVM property sets for configuring a library
Group:		Development/Java
License:	ASL 2.0
URL:		https://github.com/headius/options
Source0:	https://github.com/headius/options/archive/refs/tags/options-%{version}.tar.gz#/options-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	mvn(org.sonatype.oss:oss-parent:pom::)
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven

%description
Options reads JVM system properties into typed configuration values.
1.7 treats a blank boolean property as true, marks a forced value as
not yet loaded, and ships a Java module descriptor beside the Java 8
classes.

%prep
%autosetup -n options-options-%{version}

%files -f .mfiles
%doc LICENSE README.md
