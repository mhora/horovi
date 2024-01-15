import plone.api
from zope.component.hooks import setSite
setSite(app.Plone)

portal = plone.api.portal.get()
bubu = plone.api.content.create(container=portal, type="Document", title="Bububu")
#transaction.commit()


import pdb;pdb.set_trace()
