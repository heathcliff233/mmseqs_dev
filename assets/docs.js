(function () {
  "use strict";

  var body = document.body;
  var shell = document.getElementById("docs-shell");
  var contentPane = document.getElementById("content-pane");
  var tocContainer = document.getElementById("toc-container");
  var pageIndex = document.getElementById("page-index");
  var themeToggleBtn = document.getElementById("theme-toggle");
  var tocOpenBtn = document.getElementById("toc-open");
  var tocPane = document.getElementById("toc-pane");
  var tocBackdrop = document.getElementById("toc-backdrop");
  var backToTopBtn = document.getElementById("back-to-top");

  if (!shell || !contentPane || !tocContainer) {
    return;
  }

  markActiveProductLink();
  setupTheme(themeToggleBtn);
  movePandocContentIntoShell();

  var toc = document.getElementById("TOC");
  setupTocBranches(toc);

  var tocAnchors = getTocAnchors(toc);
  var syncTargets = collectSyncTargets(tocAnchors);
  var headings = collectHeadings();
  var indexAnchors = buildRightIndex(headings);

  setupHashNavigation(tocContainer, pageIndex);
  activateScrollSync(syncTargets, tocAnchors, indexAnchors);
  setupDrawer(tocOpenBtn, tocPane, tocBackdrop);
  setupBackToTop(backToTopBtn);
  applyInitialHashOffset();

  function markActiveProductLink() {
    var path = window.location.pathname.toLowerCase();
    var product = "";
    if (path.indexOf("/mmseqs/") !== -1) {
      product = "mmseqs";
    } else if (path.indexOf("/foldseek/") !== -1) {
      product = "foldseek";
    }

    if (product) {
      body.setAttribute("data-doc-product", product);
      var active = document.querySelector('[data-product-link="' + product + '"]');
      if (active) {
        active.classList.add("active");
      }
    }
  }

  function movePandocContentIntoShell() {
    var keepIds = {
      "docs-shell": true,
      "toc-backdrop": true,
      "back-to-top": true,
      "doc-page-footer": true
    };

    var children = Array.prototype.slice.call(body.children);
    for (var i = 0; i < children.length; i++) {
      var el = children[i];

      if (el.classList && el.classList.contains("docs-header")) {
        continue;
      }
      if (keepIds[el.id]) {
        continue;
      }
      if (el.tagName === "SCRIPT") {
        continue;
      }

      if (el.id === "TOC") {
        tocContainer.appendChild(el);
      } else {
        contentPane.appendChild(el);
      }
    }

    var tocNode = document.getElementById("TOC");
    if (tocNode) {
      tocNode.classList.add("toc-nav");
    }
  }

  function setupTheme(btn) {
    var storageKey = "docs-theme";
    var root = document.documentElement;
    var media = window.matchMedia ? window.matchMedia("(prefers-color-scheme: dark)") : null;
    var stored = readStoredTheme(storageKey);

    applyTheme(stored || (media && media.matches ? "dark" : "light"));
    refreshThemeButton(btn, root.getAttribute("data-theme") || "light");

    if (!btn) {
      return;
    }

    btn.addEventListener("click", function () {
      var current = root.getAttribute("data-theme") === "dark" ? "dark" : "light";
      var next = current === "dark" ? "light" : "dark";
      applyTheme(next);
      storeTheme(storageKey, next);
      refreshThemeButton(btn, next);
    });

    if (media && media.addEventListener) {
      media.addEventListener("change", function (event) {
        if (readStoredTheme(storageKey)) {
          return;
        }
        var theme = event.matches ? "dark" : "light";
        applyTheme(theme);
        refreshThemeButton(btn, theme);
      });
    }
  }

  function refreshThemeButton(btn, theme) {
    if (!btn) {
      return;
    }
    var isDark = theme === "dark";
    btn.textContent = isDark ? "Dark" : "Light";
    btn.setAttribute("aria-pressed", String(isDark));
    btn.setAttribute("title", isDark ? "Switch to light mode" : "Switch to dark mode");
    btn.setAttribute("data-theme-state", theme);
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute("data-theme", theme === "dark" ? "dark" : "light");
  }

  function readStoredTheme(key) {
    try {
      var value = window.localStorage.getItem(key);
      if (value === "dark" || value === "light") {
        return value;
      }
      return "";
    } catch (err) {
      return "";
    }
  }

  function storeTheme(key, value) {
    try {
      window.localStorage.setItem(key, value);
    } catch (err) {
      // Ignore storage errors (private mode / blocked storage).
    }
  }

  function setupTocBranches(tocNode) {
    if (!tocNode) {
      return;
    }

    var items = tocNode.querySelectorAll("li");
    for (var i = 0; i < items.length; i++) {
      var li = items[i];
      var link = li.querySelector(":scope > a");
      var childList = li.querySelector(":scope > ul");
      var row = li.querySelector(":scope > .toc-row");

      if (row) {
        continue;
      }

      row = document.createElement("div");
      row.className = "toc-row";

      if (childList) {
        li.classList.add("toc-branch");

        var toggle = document.createElement("button");
        toggle.type = "button";
        toggle.className = "toc-toggle";
        toggle.setAttribute("aria-label", "Toggle section");
        toggle.innerHTML = "<span aria-hidden=\"true\">▸</span>";
        row.appendChild(toggle);

        if (link) {
          link.classList.add("toc-link");
          row.appendChild(link);
        } else {
          var label = document.createElement("span");
          label.className = "toc-link toc-label";
          label.textContent = "Section";
          row.appendChild(label);
        }

        li.insertBefore(row, childList);

        var depth = getTocDepth(li);
        var collapsed = depth >= 2;
        applyBranchState(li, toggle, childList, collapsed);

        toggle.addEventListener("click", function (event) {
          event.preventDefault();
          event.stopPropagation();
          var item = this.closest("li");
          var sub = item ? item.querySelector(":scope > ul") : null;
          if (!item || !sub) {
            return;
          }
          var nowCollapsed = !item.classList.contains("collapsed");
          applyBranchState(item, this, sub, nowCollapsed);
        });
      } else if (link) {
        li.classList.add("toc-leaf");
        var spacer = document.createElement("span");
        spacer.className = "toc-spacer";
        spacer.setAttribute("aria-hidden", "true");
        row.appendChild(spacer);

        link.classList.add("toc-link");
        row.appendChild(link);
        li.insertBefore(row, li.firstChild);
      }
    }
  }

  function getTocDepth(li) {
    var depth = 0;
    var node = li.parentElement;
    while (node && node.id !== "TOC") {
      if (node.tagName === "UL") {
        depth += 1;
      }
      node = node.parentElement;
    }
    return depth;
  }

  function applyBranchState(li, btn, subList, collapsed) {
    if (!li || !btn || !subList) {
      return;
    }
    li.classList.toggle("collapsed", collapsed);
    subList.hidden = collapsed;
    btn.setAttribute("aria-expanded", String(!collapsed));
  }

  function collectHeadings() {
    var list = contentPane.querySelectorAll("h2[id], h3[id]");
    return Array.prototype.slice.call(list);
  }

  function buildRightIndex(headings) {
    if (!pageIndex) {
      return [];
    }
    pageIndex.innerHTML = "";

    if (!headings.length) {
      var empty = document.createElement("p");
      empty.className = "index-empty";
      empty.textContent = "No indexed sections";
      pageIndex.appendChild(empty);
      return [];
    }

    var list = document.createElement("ul");
    list.className = "index-list";
    var anchors = [];

    for (var i = 0; i < headings.length; i++) {
      var heading = headings[i];
      var li = document.createElement("li");
      li.className = "lvl-" + heading.tagName.toLowerCase();

      var a = document.createElement("a");
      a.href = "#" + heading.id;
      a.textContent = compactText(heading.textContent || heading.innerText || heading.id);
      li.appendChild(a);
      list.appendChild(li);
      anchors.push(a);
    }

    pageIndex.appendChild(list);
    return anchors;
  }

  function compactText(text) {
    return text.replace(/\s+/g, " ").trim();
  }

  function getTocAnchors(tocNode) {
    if (!tocNode) {
      return [];
    }
    return Array.prototype.slice.call(tocNode.querySelectorAll("a[href^='#']"));
  }

  function collectSyncTargets(tocAnchors) {
    var seen = {};
    var targets = [];

    for (var i = 0; i < tocAnchors.length; i++) {
      var href = tocAnchors[i].getAttribute("href");
      var target = getTargetFromHash(href);
      if (!target || !target.id || seen[target.id]) {
        continue;
      }
      seen[target.id] = true;
      targets.push({
        id: target.id,
        node: resolveScrollTarget(target)
      });
    }

    targets.sort(function (a, b) {
      return a.node.offsetTop - b.node.offsetTop;
    });
    return targets;
  }

  function setupHashNavigation(tocNode, indexNode) {
    function handleClick(event) {
      var link = event.target.closest("a[href^='#']");
      if (!link) {
        return;
      }

      var hash = link.getAttribute("href");
      if (!hash || hash.length < 2) {
        return;
      }

      event.preventDefault();
      if (history.pushState) {
        history.pushState(null, "", hash);
      } else {
        window.location.hash = hash;
      }
      scrollToHashTarget(hash, "auto");
    }

    if (tocNode) {
      tocNode.addEventListener("click", handleClick);
    }
    if (indexNode) {
      indexNode.addEventListener("click", handleClick);
    }

    window.addEventListener("hashchange", function () {
      scrollToHashTarget(window.location.hash, "auto");
    });
  }

  function applyInitialHashOffset() {
    if (!window.location.hash) {
      return;
    }
    window.requestAnimationFrame(function () {
      scrollToHashTarget(window.location.hash, "auto");
    });
  }

  function scrollToHashTarget(hash, behavior) {
    var target = getTargetFromHash(hash);
    if (!target) {
      return false;
    }

    var anchor = resolveScrollTarget(target);
    var offset = computeAnchorOffset();
    var y = anchor.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({
      top: Math.max(0, y),
      behavior: behavior || "auto"
    });
    return true;
  }

  function getTargetFromHash(hash) {
    if (!hash || hash.charAt(0) !== "#") {
      return null;
    }
    var id = hash.slice(1);
    if (!id) {
      return null;
    }
    try {
      id = decodeURIComponent(id);
    } catch (err) {
      return null;
    }
    return document.getElementById(id);
  }

  function resolveScrollTarget(target) {
    if (!target || target.tagName !== "SECTION") {
      return target;
    }
    var heading = target.querySelector(":scope > h1, :scope > h2, :scope > h3, :scope > h4, :scope > h5, :scope > h6");
    return heading || target;
  }

  function computeAnchorOffset() {
    var rootStyles = window.getComputedStyle(document.documentElement);
    var cssOffset = parseFloat(rootStyles.getPropertyValue("--anchor-offset"));
    if (!isNaN(cssOffset) && cssOffset > 0) {
      return Math.ceil(cssOffset);
    }
    var header = document.querySelector(".docs-header");
    var headerHeight = header ? header.getBoundingClientRect().height : 0;
    var cssGap = parseFloat(rootStyles.getPropertyValue("--anchor-gap"));
    var gap = !isNaN(cssGap) && cssGap >= 0 ? cssGap : 32;
    return Math.ceil(headerHeight + gap);
  }

  function activateScrollSync(syncTargets, tocAnchors, indexAnchors) {
    if (!syncTargets.length) {
      return;
    }

    var ticking = false;
    var activeId = "";

    function sync() {
      ticking = false;
      var next = findActiveTarget(syncTargets);
      if (!next || next.id === activeId) {
        return;
      }
      activeId = next.id;
      var activeTocLink = getVisibleTocLinkForId(tocAnchors, activeId);
      var tocHref = activeTocLink ? activeTocLink.getAttribute("href") : "";
      applyActiveLinkState(tocAnchors, tocHref);
      applyActiveLinkState(indexAnchors, "#" + activeId);
      keepElementInPaneView(activeTocLink, tocContainer);
    }

    function onScroll() {
      if (ticking) {
        return;
      }
      ticking = true;
      window.requestAnimationFrame(sync);
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    window.addEventListener("resize", onScroll);
    onScroll();
  }

  function findActiveTarget(targets) {
    var marker = window.scrollY + computeAnchorOffset() + 40;
    var current = targets[0];
    for (var i = 0; i < targets.length; i++) {
      if (targets[i].node.offsetTop <= marker) {
        current = targets[i];
      } else {
        break;
      }
    }
    return current;
  }

  function applyActiveLinkState(anchors, targetHref) {
    for (var i = 0; i < anchors.length; i++) {
      var a = anchors[i];
      a.classList.toggle("active", a.getAttribute("href") === targetHref);
    }
  }

  function getVisibleTocLinkForId(tocAnchors, id) {
    var targetHref = "#" + id;
    var link = null;
    for (var i = 0; i < tocAnchors.length; i++) {
      if (tocAnchors[i].getAttribute("href") === targetHref) {
        link = tocAnchors[i];
        break;
      }
    }
    if (!link) {
      return null;
    }

    if (isElementVisible(link)) {
      return link;
    }

    var node = link.closest("li");
    while (node && node.id !== "TOC") {
      if (node.tagName === "LI") {
        var rowLink = node.querySelector(":scope > .toc-row > .toc-link");
        if (rowLink && isElementVisible(rowLink)) {
          return rowLink;
        }
      }
      var parentList = node.parentElement;
      node = parentList ? parentList.closest("li") : null;
    }

    return null;
  }

  function isElementVisible(el) {
    return !!(el && el.getClientRects().length);
  }

  function keepElementInPaneView(el, pane) {
    if (!el || !pane) {
      return;
    }

    var paneRect = pane.getBoundingClientRect();
    var elRect = el.getBoundingClientRect();
    var viewTop = pane.scrollTop;
    var viewBottom = viewTop + pane.clientHeight;
    var itemTop = elRect.top - paneRect.top + pane.scrollTop;
    var itemBottom = itemTop + elRect.height;
    var edgePadding = Math.min(90, Math.floor(pane.clientHeight * 0.18));
    var outsideView = itemTop < viewTop + edgePadding || itemBottom > viewBottom - edgePadding;

    if (outsideView) {
      var targetTop = itemTop - (pane.clientHeight - elRect.height) / 2;
      pane.scrollTo({
        top: Math.max(0, targetTop),
        behavior: "auto"
      });
    }
  }

  function setupDrawer(openBtn, pane, backdrop) {
    if (!openBtn || !pane || !backdrop) {
      return;
    }

    function setOpen(open) {
      body.classList.toggle("toc-open", open);
      backdrop.hidden = !open;
      openBtn.setAttribute("aria-expanded", String(open));
    }

    openBtn.addEventListener("click", function () {
      setOpen(!body.classList.contains("toc-open"));
    });

    backdrop.addEventListener("click", function () {
      setOpen(false);
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") {
        setOpen(false);
      }
    });

    pane.addEventListener("click", function (event) {
      var link = event.target.closest("a[href^='#']");
      if (!link) {
        return;
      }
      if (window.matchMedia("(max-width: 1100px)").matches) {
        setOpen(false);
      }
    });
  }

  function setupBackToTop(btn) {
    if (!btn) {
      return;
    }

    function refresh() {
      btn.classList.toggle("visible", window.scrollY > 500);
    }

    btn.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });

    window.addEventListener("scroll", refresh, { passive: true });
    refresh();
  }
})();
