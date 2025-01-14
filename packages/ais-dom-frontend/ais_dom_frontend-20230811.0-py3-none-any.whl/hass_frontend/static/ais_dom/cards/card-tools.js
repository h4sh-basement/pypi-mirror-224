!(function (e) {
  var t = {};
  function r(n) {
    if (t[n]) return t[n].exports;
    var s = (t[n] = { i: n, l: !1, exports: {} });
    return e[n].call(s.exports, s, s.exports, r), (s.l = !0), s.exports;
  }
  (r.m = e),
    (r.c = t),
    (r.d = function (e, t, n) {
      r.o(e, t) || Object.defineProperty(e, t, { enumerable: !0, get: n });
    }),
    (r.r = function (e) {
      "undefined" != typeof Symbol &&
        Symbol.toStringTag &&
        Object.defineProperty(e, Symbol.toStringTag, { value: "Module" }),
        Object.defineProperty(e, "__esModule", { value: !0 });
    }),
    (r.t = function (e, t) {
      if ((1 & t && (e = r(e)), 8 & t)) return e;
      if (4 & t && "object" == typeof e && e && e.__esModule) return e;
      var n = Object.create(null);
      if (
        (r.r(n),
        Object.defineProperty(n, "default", { enumerable: !0, value: e }),
        2 & t && "string" != typeof e)
      )
        for (var s in e)
          r.d(
            n,
            s,
            function (t) {
              return e[t];
            }.bind(null, s)
          );
      return n;
    }),
    (r.n = function (e) {
      var t =
        e && e.__esModule
          ? function () {
              return e.default;
            }
          : function () {
              return e;
            };
      return r.d(t, "a", t), t;
    }),
    (r.o = function (e, t) {
      return Object.prototype.hasOwnProperty.call(e, t);
    }),
    (r.p = ""),
    r((r.s = 3));
})([
  function (e, t, r) {
    "use strict";
    function n() {
      return document.querySelector("home-assistant").hass;
    }
    function s(e) {
      return document.querySelector("home-assistant").provideHass(e);
    }
    function o() {
      var e = document.querySelector("home-assistant");
      if (
        (e =
          (e =
            (e =
              (e =
                ((e =
                  (e =
                    (e =
                      (e = e && e.shadowRoot) &&
                      e.querySelector("home-assistant-main")) &&
                    e.shadowRoot) &&
                  e.querySelector(
                    "app-drawer-layout partial-panel-resolver"
                  )) &&
                  e.shadowRoot) ||
                e) && e.querySelector("ha-panel-lovelace")) && e.shadowRoot) &&
          e.querySelector("hui-root"))
      ) {
        var t = e.lovelace;
        return (t.current_view = e.___curView), t;
      }
      return null;
    }
    function a() {
      var e = document.querySelector("home-assistant");
      return (e =
        (e =
          (e =
            (e =
              (e =
                (e =
                  (e =
                    ((e =
                      (e =
                        (e =
                          (e = e && e.shadowRoot) &&
                          e.querySelector("home-assistant-main")) &&
                        e.shadowRoot) &&
                      e.querySelector(
                        "app-drawer-layout partial-panel-resolver"
                      )) &&
                      e.shadowRoot) ||
                    e) && e.querySelector("ha-panel-lovelace")) &&
                e.shadowRoot) && e.querySelector("hui-root")) &&
            e.shadowRoot) && e.querySelector("ha-app-layout #view")) &&
        e.firstElementChild);
    }
    r.d(t, "a", function () {
      return n;
    }),
      r.d(t, "d", function () {
        return s;
      }),
      r.d(t, "b", function () {
        return o;
      }),
      r.d(t, "c", function () {
        return a;
      });
  },
  function (e, t, r) {
    "use strict";
    r.d(t, "a", function () {
      return n;
    });
    let n = (function () {
      if (window.fully && "function" == typeof fully.getDeviceId)
        return fully.getDeviceId();
      if (!localStorage["lovelace-player-device-id"]) {
        const e = () =>
          Math.floor(1e5 * (1 + Math.random()))
            .toString(16)
            .substring(1);
        localStorage["lovelace-player-device-id"] = `${e()}${e()}-${e()}${e()}`;
      }
      return localStorage["lovelace-player-device-id"];
    })();
  },
  function (module, __webpack_exports__, __webpack_require__) {
    "use strict";
    __webpack_require__.d(__webpack_exports__, "a", function () {
      return hasOldTemplate;
    }),
      __webpack_require__.d(__webpack_exports__, "b", function () {
        return parseOldTemplate;
      });
    var _hass_js__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(0),
      _deviceID_js__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(1);
    function hasOldTemplate(e) {
      return /\[\[\s+.*\s+\]\]/.test(e);
    }
    function parseTemplateString(str, specialData = {}) {
      if ("string" != typeof str) return text;
      const FUNCTION = /^[a-zA-Z0-9_]+\(.*\)$/,
        EXPR = /([^=<>!]+)\s*(==|!=|<|>|<=|>=)\s*([^=<>!]+)/,
        SPECIAL = /^\{.+\}$/,
        STRING = /^"[^"]*"|'[^']*'$/;
      "string" == typeof specialData && (specialData = {}),
        (specialData = Object.assign(
          {
            user: Object(_hass_js__WEBPACK_IMPORTED_MODULE_0__.a)().user.name,
            browser: _deviceID_js__WEBPACK_IMPORTED_MODULE_1__.a,
            hash: location.hash.substr(1) || " ",
          },
          specialData
        ));
      const _parse_function = (e) => {
          let t = [e.substr(0, e.indexOf("(")).trim()];
          for (e = e.substr(e.indexOf("(") + 1); e; ) {
            let r = 0,
              n = 0,
              s = !1;
            for (; e[r]; ) {
              let t = e[r++];
              if (
                (t === s && r > 1 && "\\" !== e[r - 2]
                  ? (s = !1)
                  : "\"'".includes(t) && (s = t),
                !s)
              ) {
                if ("(" === t) n += 1;
                else if (")" === t) {
                  n -= 1;
                  continue;
                }
                if (!(n > 0) && ",)".includes(t)) break;
              }
            }
            t.push(e.substr(0, r - 1).trim()), (e = e.substr(r));
          }
          return t;
        },
        _parse_special = (e) => (
          (e = e.substr(1, e.length - 2)), specialData[e] || `{${e}}`
        ),
        _parse_entity = (e) => {
          let t;
          if ((e = e.split("."))[0].match(SPECIAL))
            (t = _parse_special(e.shift())),
              (t =
                Object(_hass_js__WEBPACK_IMPORTED_MODULE_0__.a)().states[t] ||
                t);
          else if (
            ((t = Object(_hass_js__WEBPACK_IMPORTED_MODULE_0__.a)().states[
              `${e.shift()}.${e.shift()}`
            ]),
            !e.length)
          )
            return t.state;
          return e.forEach((e) => (t = t[e])), t;
        },
        _eval_expr = (str) => {
          if (((str = EXPR.exec(str)), null === str)) return !1;
          const lhs = parseTemplateString(str[1]),
            rhs = parseTemplateString(str[3]);
          var expr = "";
          return (
            (expr =
              parseFloat(lhs) != lhs
                ? `"${lhs}" ${str[2]} "${rhs}"`
                : `${parseFloat(lhs)} ${str[2]} ${parseFloat(rhs)}`),
            eval(expr)
          );
        },
        _eval_function = (e) => {
          if ("if" === e[0])
            return _eval_expr(e[1])
              ? parseTemplateString(e[2])
              : parseTemplateString(e[3]);
        };
      try {
        return (
          (str = str.trim()),
          str.match(STRING)
            ? str.substr(1, str.length - 2)
            : str.match(SPECIAL)
            ? _parse_special(str)
            : str.match(FUNCTION)
            ? _eval_function(_parse_function(str))
            : str.includes(".")
            ? _parse_entity(str)
            : str
        );
      } catch (e) {
        return `[[ Template matching failed: ${str} ]]`;
      }
    }
    function parseOldTemplate(e, t = {}) {
      if ("string" != typeof e) return e;
      return (e = e.replace(/\[\[\s(.*?)\s\]\]/g, (e, r, n, s) =>
        parseTemplateString(r, t)
      ));
    }
  },
  function (e, t, r) {
    "use strict";
    r.r(t);
    const n = customElements.get("home-assistant-main")
        ? Object.getPrototypeOf(customElements.get("home-assistant-main"))
        : Object.getPrototypeOf(customElements.get("hui-view")),
      s = n.prototype.html,
      o = n.prototype.css;
    function a(e, t, r = null) {
      if (
        (((e = new Event(e, {
          bubbles: !0,
          cancelable: !1,
          composed: !0,
        })).detail = t || {}),
        r)
      )
        r.dispatchEvent(e);
      else {
        var n = document.querySelector("home-assistant");
        (n =
          (n =
            (n =
              (n =
                (n =
                  (n =
                    (n =
                      ((n =
                        (n =
                          (n =
                            (n = n && n.shadowRoot) &&
                            n.querySelector("home-assistant-main")) &&
                          n.shadowRoot) &&
                        n.querySelector(
                          "app-drawer-layout partial-panel-resolver"
                        )) &&
                        n.shadowRoot) ||
                      n) && n.querySelector("ha-panel-lovelace")) &&
                  n.shadowRoot) && n.querySelector("hui-root")) &&
              n.shadowRoot) && n.querySelector("ha-app-layout #view")) &&
          n.firstElementChild) && n.dispatchEvent(e);
      }
    }
    const i = "custom:";
    function c(e, t) {
      const r = document.createElement("hui-error-card");
      return r.setConfig({ type: "error", error: e, config: t }), r;
    }
    function l(e, t) {
      if (!t || "object" != typeof t || !t.type)
        return c(`No ${e} type configured`, t);
      let r = t.type;
      if (
        ((r = r.startsWith(i) ? r.substr(i.length) : `hui-${r}-${e}`),
        customElements.get(r))
      )
        return (function (e, t) {
          const r = document.createElement(e);
          try {
            r.setConfig(t);
          } catch (e) {
            return c(e, t);
          }
          return r;
        })(r, t);
      const n = c(`Custom element doesn't exist: ${r}.`, t);
      n.style.display = "None";
      const s = setTimeout(() => {
        n.style.display = "";
      }, 2e3);
      return (
        customElements.whenDefined(r).then(() => {
          clearTimeout(s), a("ll-rebuild", {}, n);
        }),
        n
      );
    }
    function u(e) {
      return l("card", e);
    }
    function p(e) {
      return l("element", e);
    }
    function d(e) {
      const t = new Set(["call-service", "divider", "section", "weblink"]);
      if (!e) return c("Invalid configuration given.", e);
      if (
        ("string" == typeof e && (e = { entity: e }),
        "object" != typeof e || (!e.entity && !e.type))
      )
        return c("Invalid configuration given.", e);
      const r = e.type || "default";
      if (t.has(r) || r.startsWith(i)) return l("row", e);
      const n = e.entity.split(".", 1)[0];
      return (
        Object.assign(e, {
          type:
            {
              alert: "toggle",
              automation: "toggle",
              climate: "climate",
              cover: "cover",
              fan: "toggle",
              group: "group",
              input_boolean: "toggle",
              input_number: "input-number",
              input_select: "input-select",
              input_text: "input-text",
              light: "toggle",
              lock: "lock",
              media_player: "media-player",
              remote: "toggle",
              scene: "scene",
              script: "script",
              sensor: "sensor",
              timer: "timer",
              switch: "toggle",
              vacuum: "toggle",
              water_heater: "climate",
              input_datetime: "input-datetime",
            }[n] || "text",
        }),
        l("entity-row", e)
      );
    }
    var m = r(0);
    class f extends n {
      static get properties() {
        return { hass: {}, config: {}, noHass: { type: Boolean } };
      }
      setConfig(e) {
        (this._config = e),
          this.el ? this.el.setConfig(e) : (this.el = this.create(e)),
          this._hass && (this.el.hass = this._hass),
          this.noHass && Object(m.d)(this);
      }
      set config(e) {
        this.setConfig(e);
      }
      set hass(e) {
        (this._hass = e), this.el && (this.el.hass = e);
      }
      createRenderRoot() {
        return this;
      }
      render() {
        return s`${this.el}`;
      }
    }
    if (!customElements.get("card-maker")) {
      class e extends f {
        create(e) {
          return u(e);
        }
      }
      customElements.define("card-maker", e);
    }
    if (!customElements.get("element-maker")) {
      class e extends f {
        create(e) {
          return p(e);
        }
      }
      customElements.define("element-maker", e);
    }
    if (!customElements.get("entity-row-maker")) {
      class e extends f {
        create(e) {
          return d(e);
        }
      }
      customElements.define("entity-row-maker", e);
    }
    var h = r(1);
    function _(e, t = {}) {
      return (
        customElements.whenDefined("long-press").then(() => {
          document.body.querySelector("long-press").bind(e);
        }),
        customElements.whenDefined("action-handler").then(() => {
          document.body.querySelector("action-handler").bind(e, t);
        }),
        e
      );
    }
    function g(e, t = !1) {
      a(
        "hass-more-info",
        { entityId: e },
        document.querySelector("home-assistant")
      );
      const r = document.querySelector("home-assistant")._moreInfoEl;
      return (r.large = t), r;
    }
    function y() {
      const e =
        document.querySelector("home-assistant") &&
        document.querySelector("home-assistant")._moreInfoEl;
      e && e.close();
    }
    function b(e, t, r = !1, n = null, s = !1) {
      a("hass-more-info", { entityId: null });
      const o = document.querySelector("home-assistant")._moreInfoEl;
      o.close(), o.open();
      const i = document.createElement("div");
      i.innerHTML = `\n  <style>\n    app-toolbar {\n      color: var(--more-info-header-color);\n      background-color: var(--more-info-header-background);\n    }\n    .scrollable {\n      overflow: auto;\n      max-width: 100% !important;\n    }\n  </style>\n  ${
        s
          ? ""
          : `\n      <app-toolbar>\n        <paper-icon-button\n          icon="hass:close"\n          dialog-dismiss=""\n        ></paper-icon-button>\n        <div class="main-title" main-title="">\n          ${e}\n        </div>\n      </app-toolbar>\n      `
      }\n    <div class="scrollable">\n      <card-maker nohass>\n      </card-maker>\n    </div>\n  `;
      const c = i.querySelector(".scrollable");
      (c.querySelector("card-maker").config = t),
        (o.sizingTarget = c),
        (o.large = r),
        (o._page = "none"),
        o.shadowRoot.appendChild(i);
      let l = {};
      if (n)
        for (var u in (o.resetFit(), n))
          (l[u] = o.style[u]), o.style.setProperty(u, n[u]);
      return (
        (o._dialogOpenChanged = function (e) {
          if (
            !e &&
            (this.stateObj && this.fire("hass-more-info", { entityId: null }),
            this.shadowRoot == i.parentNode &&
              ((this._page = null), this.shadowRoot.removeChild(i), n))
          )
            for (var t in (o.resetFit(), l))
              l[t] ? o.style.setProperty(t, l[t]) : o.style.removeProperty(t);
        }),
        o
      );
    }
    function v(e, t, r) {
      e || (e = Object(m.a)().connection);
      let n = {
          user: Object(m.a)().user.name,
          browser: h.a,
          hash: location.hash.substr(1) || " ",
          ...r.variables,
        },
        s = r.template,
        o = r.entity_ids;
      return e.subscribeMessage((e) => t(e.result), {
        type: "render_template",
        template: s,
        variables: n,
        entity_ids: o,
      });
    }
    var w = r(2);
    class E {
      static checkVersion(e) {}
      static get deviceID() {
        return h.a;
      }
      static get fireEvent() {
        return a;
      }
      static get hass() {
        return Object(m.a)();
      }
      static get lovelace() {
        return Object(m.b)();
      }
      static get lovelace_view() {
        return m.c;
      }
      static get provideHass() {
        return m.d;
      }
      static get LitElement() {
        return n;
      }
      static get LitHtml() {
        return s;
      }
      static get LitCSS() {
        return o;
      }
      static get longpress() {
        return _;
      }
      static get createCard() {
        return u;
      }
      static get createElement() {
        return p;
      }
      static get createEntityRow() {
        return d;
      }
      static get moreInfo() {
        return g;
      }
      static get popUp() {
        return b;
      }
      static get closePopUp() {
        return y;
      }
      static get hasTemplate() {
        return w.a;
      }
      static parseTemplate(e, t, r = {}) {
        return "string" == typeof e
          ? Object(w.b)(e, t)
          : (async function (e, t, r = {}) {
              for (var n in (e || (e = e()),
              (r = {}),
              (r = Object.assign(
                {
                  user: e.user.name,
                  browser: h.a,
                  hash: location.hash.substr(1) || " ",
                },
                r
              )))) {
                var s = new RegExp(`\\{${n}\\}`, "g");
                t = t.replace(s, r[n]);
              }
              return e.callApi("POST", "template", { template: t });
            })(e, t, r);
      }
      static get subscribeRenderTemplate() {
        return v;
      }
    }
    customElements.get("card-tools") ||
      (customElements.define("card-tools", E),
      (window.cardTools = customElements.get("card-tools")),
      console.info(
        `%cCARD-TOOLS 2 IS INSTALLED\n  %cDeviceID: ${
          customElements.get("card-tools").deviceID
        }`,
        "color: green; font-weight: bold",
        ""
      ));
  },
]);
