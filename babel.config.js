module.exports = {
  // "presets": ["@babel/env", "@babel/typescript"],
  "plugins": [
    // "@babel/helper-split-export-declaration'",
    "@babel/proposal-object-rest-spread",
    "@babel/plugin-transform-modules-commonjs",
    "@babel/plugin-transform-typescript",
    ["@babel/plugin-proposal-decorators", { "legacy": true }],
    ["@babel/plugin-proposal-class-properties", { "loose": true }]
  ]
}