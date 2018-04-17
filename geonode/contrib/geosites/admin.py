# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.contrib import admin

from .models import SiteResources, SitePeople, SiteGroups


class SiteResourceAdmin(admin.ModelAdmin):
    filter_horizontal = ('resources',)
    readonly_fields = ('site',)


class SitePeopleAdmin(admin.ModelAdmin):
    filter_horizontal = ('people',)
    readonly_fields = ('site',)


class SiteGroupAdmin(admin.ModelAdmin):
    filter_horizontal = ('group',)
    readonly_fields = ('site',)


admin.site.register(SiteResources, SiteResourceAdmin)
admin.site.register(SitePeople, SitePeopleAdmin)
admin.site.register(SiteGroups, SiteGroupAdmin)
