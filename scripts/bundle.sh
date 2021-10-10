#!/usr/local/bin/bash
NODE_ENV=production
TAILWIND_MODE=build
npx tailwindcss -o ./app/static/css/tailwind.css --jit --minify