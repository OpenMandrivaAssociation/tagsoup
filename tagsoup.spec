Name:          tagsoup
Version:       1.2.1
Release:       1
Summary:       A SAX-compliant parser written in Java
Group:         Development/Java
License:       ASL, GPL
Url:           http://home.ccil.org/~cowan/XML/%{name}/
Source0:       http://home.ccil.org/~cowan/XML/%{name}/%{name}-%{version}-src.zip
Source1:       http://repo1.maven.org/maven2/org/ccil/cowan/tagsoup/tagsoup/%{version}/tagsoup-%{version}.pom
BuildRequires: ant
BuildRequires: saxon >= 6.5.5
BuildRequires: jpackage-utils
BuildRequires: java-devel
BuildRequires: java-javadoc
BuildRequires: xalan-j2
Requires:      java
Requires:      jpackage-utils
BuildArch:     noarch

%description
TagSoup is a SAX-compliant parser written in Java
that, instead of parsing well-formed or valid XML,
parses HTML as it is found in the wild: nasty and
brutish, though quite often far from short. TagSoup
is designed for people who have to process this stuff
using some semblance of a rational application design.
By providing a SAX interface, it allows standard XML
tools to be applied to even the worst HTML.

%package javadoc
Group:          Development/Java
Summary:        Javadoc for %{name}

%description javadoc
TagSoup - A SAX-compliant parser written in Java.

This package contains javadoc for %{name}.

%prep
%setup -q -n tagsoup-%{version}

find . -name '*.jar' -exec rm -f '{}' \;
find . -name '*.class' -exec rm -f '{}' \;

%build
export CLASSPATH=$(build-classpath xalan-j2 xalan-j2-serializer saxon ant):build
ant \
  -Dtagsoup.version=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  dist docs-api

%install

mkdir -p %{buildroot}%{_javadir}
install -m 644 dist/lib/%{name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/api/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/

%files
%{_javadir}/%{name}.jar
%{_mandir}/man1/%{name}.1.xz
%{_datadir}/maven2/poms/JPP-%{name}.pom
%doc CHANGES LICENSE README TODO %{name}.txt

%pre javadoc
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files javadoc
%{_javadocdir}/%{name}
