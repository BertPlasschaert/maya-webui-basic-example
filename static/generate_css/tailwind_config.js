/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../index.html"
  ],
  theme: {
    extend: {
      colors: {
        "maya": {
          "viewport": "#5c5c5c",
          "white": "#efefef",
          "light": "#bbbbbb",
          "medium": "#5d5d5d",
          "default": "#444444",
          "dark": "#373737",
          "darker": "#2a2a2a"
        },
      },
    },
  },
}
