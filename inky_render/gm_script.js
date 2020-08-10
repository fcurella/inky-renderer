// ==UserScript==
// @name         On Call
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Shows different screen when a URL loads/unloads
// @author       Flavio Curella
// @match        https://meet.google.com/*
// @grant unsafeWindow
// @grant window.close
// @grant window.onbeforeunload
// @grant GM_xmlhttpRequest
// @connect raspberrypi.local
// ==/UserScript==

(function() {
    'use strict';

    const apiURL = "http://raspberrypi.local/api/screens/"
    const offCallId = 5;
    const onCallId = 4;

    const show = (picId) => (
        GM_xmlhttpRequest(
            {
                url: `${apiURL}${picId}/show/`,
                method: "POST",
            }
        )
    );

    window.addEventListener('beforeunload', () => show(offCallId))

    show(onCallId);

})();
