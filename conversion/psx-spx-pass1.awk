# Removes extra spaces off a string
function ltrim(s) { sub(/^[ \t\r\n]+/, "", s); return s; }
function rtrim(s) { sub(/[ \t\r\n]+$/, "", s); return s; }
function trim(s) { return rtrim(ltrim(s)); }

# Escape slashes and amps in a string for building links
function linkescape(s) {
    gsub(/\//, "\\/", s);
    gsub(/&/, "\\\\&", s);
    return s;
}

# Creates a section link using normal replacement rules
function nametolink(s) {
    s = tolower(s);
    gsub(/[^a-z0-9 -]/, "", s);
    gsub(/ /, "-", s);
    return s;
}

BEGIN {
    sectionCount = 0;
    WAIT_FOR_START = 1;
    IN_PRE = 0;
}

# PARSE_HEADERS will be true only for the TOC list of HREFs
# so we can build the list of "chapters".
PARSE_HEADERS && /<A HREF=/ {
    match($0, /"#(.*)">(.*)<.A/, m);
    sections[sectionCount] = m[2];
    sectionsLink[sectionCount] = m[1];
    sectionCount++;
    next;
}

# This marks the beginning of the TOC really.
WAIT_FOR_START && /<B>Nocash PSXSPX Playstation Specifications<.B><BR>/ {
    PARSE_HEADERS = 1;
    next;
}

# These markers are to split off sections and subsections.
/^<!--------------------------------------->/ {
    if (PARSE_HEADERS) WAIT_FOR_START = 0;
    PARSE_HEADERS = 0;
    WAIT_SECTION = 1;
    next;
}

# Trash anything that's in the TOC. We'll build a new one later.
WAIT_FOR_START { next; }

# We need to do slighly different parsing if we're in or out a PRE section.
/<TABLE.*PRE>/ { IN_PRE = 1; }
/<.TD><.TR><.TABLE>/ { IN_PRE = 0; }

# Generic sed-like line replacements.
{
    # The input file isn't valid html to begin with,
    # so we're not going to do a true html parser.
    # Replace the typical html escapes right off the bat.
    gsub(/&nbsp;/, " ");
    if (IN_PRE) {
        gsub(/&lt;/, "<");
        gsub(/&gt;/, ">");
    } else {
        # outside of <PRE> blocks, we want to escape these for the md format.
        gsub(/&lt;/, "\\<");
        gsub(/&gt;/, "\\>");
        gsub(/*/, "\\*");
        gsub(/_/, "\\_");
        gsub(/~/, "\\~");
    }
    gsub(/&amp;/, "\\&");

    # These are fairly straightforward replacements
    sub(/<TABLE.*PRE>/, "```");
    sub(/<.TD><.TR><.TABLE>/, "```");
    $0 = gensub(/<B>(.*)<.B><BR>/, "#### \\1", "g");
    sub(/<BR>/, "<br/>");
}

# Skip the remaining cruft.
/^<TABLE/ { next; }
/^<.FONT/ { next; }

# We need to parse the header of a major or minor section.
WAIT_SECTION {
    WAIT_SECTION = 0;
    WAIT_HEADER = 1;
    match($0, /<A NAME="(.*)">/, m);
    link = m[1];
    found = 0;
    # Checking if it was in our TOC to distingish between section or subsection.
    for (i = 0; i < sectionCount; i++) {
        if (sectionsLink[i] == link) {
            GOT_MAJOR_SECTION = 1;
            sectionFile = link;
            found = 1;
            subsectionsCount = 0;
            printf("SWITCHED TO MAJOR SECTION: %s\n", link);
        }
    }
    if (!found) {
        subsection = link;
        printf("SWITCHED TO MINOR SECTION: %s\n", link);
    }
    next;
}

# Creating the proper section header, and the second pass sed script.
WAIT_HEADER {
    WAIT_HEADER = 0;
    if (GOT_MAJOR_SECTION) {
        print("s/<A HREF=\"#" link "\">[^<]*<.A>/[" linkescape(trim($0)) "](" link ".md)/g") > "psx-spx-pass2.sed";
        $0 = "# " $0;
    } else {
        print("s/<A HREF=\"#" link "\">[^<]*<.A>/[" linkescape(trim($0)) "](" sectionFile ".md#" nametolink(trim($0)) ")/g") > "psx-spx-pass2.sed";
        $0 = "## " $0;
    }

    GOT_MAJOR_SECTION = 0;
}

# If we get here, output our current line to the current section md file.
{ print > sectionFile ".md" }

END {
    # Emit the TOC and finish the second pass sed script, as well as
    # the second pass runner script.
    for (i = 0; i < sectionCount; i++) {
        link = sectionsLink[i];
        name = sections[i];
        print("sed -f psx-spx-pass2.sed -i " link ".md") > "run-pass2.sh";
        print("[" name "](" link ".md)<br/>") > "index.md";
    }

    print("s/^<br\\/>$//") > "psx-spx-pass2.sed";
}
