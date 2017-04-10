\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{lab}
\LoadClass{article}
\RequirePackage[margin=1in]{geometry}  % Set page margins
\RequirePackage{graphicx}
\RequirePackage{caption}               % Go to top of image when Fig. is clicked
\RequirePackage{subcaption}            % Subfigure labels
\RequirePackage{color}                 % Color text
\RequirePackage[nottoc]{tocbibind}     % Add references to TOC
\RequirePackage{hyperref}              % Hyperlinks
\hypersetup{
    colorlinks=true,
    urlcolor=blue,
    citecolor=magenta,
    linkcolor=magenta,
}
\RequirePackage[numbers]{natbib}

\date{}
\author{}

\newcommand*{\labacronym}[1]{\gdef\@labacronym{#1}}
\newcommand*{\@labacronym}{\texttt{\string\labacronym} currently not set.}
\newcommand*{\labtitle}[1]{\gdef\@labtitle{#1}}
\newcommand*{\@labtitle}{\texttt{\string\labtitle} currently not set.}
\renewcommand*{\maketitle}{\newpage
    \begin{center}
    {\LARGE \@labacronym\ - \@labtitle} \par \vspace{.5em}
    {\Large Physics 111B: Advanced Experimentation Laboratory \par \vspace{.5em}
    University of California, Berkeley}
    \end{center}
    \vspace{1.5em}
}

\newcommand{\AdvancedLabSyllabus}{http://experimentationlab.berkeley.edu/syllabus}
\newcommand{\MailDonOrlando}{mailto:phylabs@berkeley.edu}
\newcommand{\ErrorAnalysisVideo}{https://www.youtube.com/watch?v=jR54387Wd6c}
\newcommand{\ErrorAnalysisNotes}{http://experimentationlab.berkeley.edu/EAX}
\newcommand{\ExperimentEvaluation}{http://experimentationlab.berkeley.edu/StudentEvaluation}
\newcommand{\LabReprints}{http://physics111.lib.berkeley.edu/Physics111/}
