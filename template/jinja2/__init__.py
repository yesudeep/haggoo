#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Template rendering function using Jinja2. 
# Copyright (c) 2009 happychickoo.
#
# The MIT License
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

__all__ = ["render_generator", "render"]

from haggoo.template.jinja2.filters import datetimeformat
from jinja2 import Environment, FileSystemLoader
from urllib import urlencode

default_filters = {
    'urlencode': urlencode,
    'datetimeformat': datetimeformat,
}

def render_generator(loader=FileSystemLoader,
                     directories=['templates'],
                     filters=default_filters,
                     builtins=None):
    """Creates a render Jinja2 function based on given arguments."""
    env = Environment(loader=loader(directories))
    env.filters.update(filters)

    if builtins == None:
        builtins = {}
    
    def render_template(template_name, **context):
        """
        Fills a template with values provided as context.
    
        The function also includes a few template builtins that are available to all 
        rendered templates.
    
        """
        template = env.get_template(template_name)
        new_context = {}
        new_context.update(builtins)
        new_context.update(context)
        return template.render(new_context)
    
    return render_template

# Convenience default template renderer.
render = render_generator()
