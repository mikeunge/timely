#!/usr/bin/bash
NODE_ENV=production
TAILWIND_MODE=build
postcss app/timely/static/css/styles.css -o app/timely/static/css/tailwind.css