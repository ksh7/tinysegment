// tinySegment.js

var apiUrl = '';
var elementTrackingEvents = [];

function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

function updateComponent(element_id, html_content) {
    var parentDiv = document.getElementById(element_id);
    parentDiv.innerHTML = html_content;
}

function getValueByKey(key) {
  for (const obj of elementTrackingEvents) {
    if (key in obj) {
      return obj[key];
    }
  }
  return null;
}


function fetchTinySegment(element_id) {
    let segment_anon_id = localStorage.getItem("ajs_anonymous_id");
    var mapEleId = getValueByKey(element_id);
    const postData = {
        segment_anon_id: segment_anon_id,
        element_id: element_id,
        source_event: mapEleId
    };
    const requestOptions = {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(postData)
    };

    fetch(apiUrl, requestOptions)
        .then(response => response.json())
        .then(data => {
            updateComponent(element_id, data.html_content);
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function onElementInView(element_id) {
    var mapEleId = getValueByKey(element_id);
    if (!mapEleId) {
      return null;
    }
    analytics.track(mapEleId, {
        element_id: element_id
    });
    // call API with anon id
    fetchTinySegment(element_id);
}

function handleScroll(targetElement) {
    if (targetElement && isInViewport(targetElement)) {
        if (!targetElement.dataset.inViewport) {
            targetElement.dataset.inViewport = true;
            setTimeout(() => {
                if (isInViewport(targetElement)) {
                    onElementInView(targetElement.id);
                }
                delete targetElement.dataset.inViewport;
            }, 5000);
        }
    }
}

function initializeElments(elementIds) {
    if (!Array.isArray(elementIds)) {
        return;
    }
    elementIds.forEach(elementId => {
        const targetElement = document.getElementById(elementId);
        if (targetElement) {
            window.addEventListener('scroll', () => handleScroll(targetElement));
            document.addEventListener('DOMContentLoaded', () => handleScroll(targetElement));
        } else {
            console.error(`Element with ID '${elementId}' not found.`);
        }
    });
}

function initializeEvents(_elementTrackingEvents) {
  elementTrackingEvents =  _elementTrackingEvents;
}

function initializeAPIUrl(_apiUrl) {
  apiUrl = _apiUrl;
}

const tinySegmentScrollObserver = {
  initializeElments: initializeElments
};

const tinySegmentElementTracking = {
  initializeEvents: initializeEvents
};

const tinySegmentAPIURL = {
  initializeAPIUrl: initializeAPIUrl
};