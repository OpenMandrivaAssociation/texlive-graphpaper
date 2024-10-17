Name:		texlive-graphpaper
Version:	63116
Release:	2
Summary:	A LaTeX class to generate several types of graph papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/graphpaper
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphpaper.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphpaper.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphpaper.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Graphpaper is a LaTeX document class which allows to print
several types of graph papers: bilinear (millimeter paper),
semilogarithmic, bilogarithmic, polar, log-polar, Smith charts.
It is based on the picture environment and its extensions.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/graphpaper
%{_texmfdistdir}/tex/latex/graphpaper
%doc %{_texmfdistdir}/doc/latex/graphpaper

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
