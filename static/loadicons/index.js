function handleError(string) {
    string = 'loadIcons: ' + string;
    const error = new Error(string);

    console.error(error.toString());
}

function injectSVG(svgURL) {
    // 200 for web servers, 0 for CEP panels
    if (this.status !== 200 && this.status !== 0) {
        handleError('Failed to fetch icons, server returned ' + this.status);
        return;
    }

    // Parse the SVG
    const parser = new DOMParser();
    try {
        const doc = parser.parseFromString(this.responseText, 'image/svg+xml');
        var svg = doc.firstChild;
    } catch (err) {
        handleError('Error parsing SVG: ' + err);
        return;
    }

    // Make sure a real SVG was returned
    if (svg && svg.tagName === 'svg') {
        // Hide the element
        svg.style.display = 'none';

        svg.setAttribute('data-url', svgURL);

        // Insert it into the head
        document.head.insertBefore(svg, null);
    } else {
        handleError('Parsed SVG document contained something other than an SVG');
    }
}

export default function (svgURL) {
    // Request the SVG sprite
    const req = new XMLHttpRequest();
    req.open('GET', svgURL, true);
    req.addEventListener('load', injectSVG.bind(req, svgURL));
    req.addEventListener('error', function (event) {
        handleError('Request failed');
    });
    req.send();
}
