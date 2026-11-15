Name:		options
Version:	1.7
Release:	2
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

%check -a
mkdir -p chk
cat > chk/OptionsCheck.java << 'EOF'
import com.headius.options.Option;

public class OptionsCheck {
	enum Cat {
		CHECK
	}

	public static void main(String[] args) {
		System.setProperty("options.check", "7");
		Option<Integer> width = Option.integer("options.check", Cat.CHECK, Integer.valueOf(1), "width");
		Integer loaded = width.load();
		if (loaded == null || loaded.intValue() != 7) {
			throw new RuntimeException("width " + loaded);
		}
		System.setProperty("options.flag", "");
		Option<Boolean> flag = Option.bool("options.flag", Cat.CHECK, Boolean.FALSE, "flag");
		if (!Boolean.TRUE.equals(flag.load())) {
			throw new RuntimeException("blank flag");
		}
		System.out.println("options_ok %{version} " + loaded);
	}
}
EOF
test -s target/options-%{version}.jar
javac -cp target/options-%{version}.jar -d chk chk/OptionsCheck.java
java -cp chk:target/options-%{version}.jar OptionsCheck > chk/out.txt
cat chk/out.txt
grep -q '^options_ok %{version} 7$' chk/out.txt

%files -f .mfiles
%doc LICENSE README.md
