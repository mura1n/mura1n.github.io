#!/usr/bin/env bash
# Sourced only by this site's scripts. Does not modify the system Ruby.
export RUBYOPT="${RUBYOPT:+$RUBYOPT }-EUTF-8"
site_ruby_cache="${HOME}/.cache/refineedit-homepage-ruby26"
if [[ "$(ruby -e 'print RUBY_VERSION' 2>/dev/null)" == 2.6.* && -f "$site_ruby_cache/bin/bundle" ]]; then
  export GEM_HOME="$site_ruby_cache"
  export GEM_PATH="$site_ruby_cache:/Library/Ruby/Gems/2.6.0:/System/Library/Frameworks/Ruby.framework/Versions/2.6/usr/lib/ruby/gems/2.6.0"
  export BUNDLE_PATH="$site_ruby_cache/bundle"
  site_bundle=(ruby "$site_ruby_cache/bin/bundle")
else
  site_bundle=(bundle)
fi
