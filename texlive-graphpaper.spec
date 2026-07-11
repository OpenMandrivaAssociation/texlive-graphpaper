%global tl_name graphpaper
%global tl_revision 63116

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	A LaTeX class to generate several types of graph papers
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/graphpaper
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphpaper.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphpaper.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphpaper.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Graphpaper is a LaTeX document class which allows to print several types
of graph papers: bilinear (millimeter paper), semilogarithmic,
bilogarithmic, polar, log-polar, Smith charts. It is based on the
picture environment and its extensions.

