from azure.storage.blob import BlockBlobService
block_blob_service = BlockBlobService(account_name='animalstorage', account_key='Wkoeuit9Ub0PREAPmCM43EaGGkeCwl+EMjMGC8eg6lWk8iUNC8iJEFPscCgMAHXVhR5l1q/u1ChERDKAx+vGCw==')


from azure.storage.blob import ContentSettings
def azureBlobPhotoP(filepath,photoName):
    block_blob_service.create_blob_from_path(
    'photocontainer',
     filepath,
     photoName,
    content_settings=ContentSettings(content_type='image/png')
            )
    return block_blob_service.make_blob_url("photocontainer", filepath)
#azureBlobPhotoP("myblobcat4","cat4.png")
#azureBlobPhotoP("myblobcat2","cat2.png")
def azureBlobPhotoJ(filepath,photoName):
    block_blob_service.create_blob_from_path(
    'photocontainer',
     filepath,
     photoName,
    content_settings=ContentSettings(content_type='image/jpg')
            )
    return block_blob_service.make_blob_url("photocontainer", filepath)

    #print(block_blob_service.make_blob_url("photocontainer", "myblobcat3"))
print(azureBlobPhotoJ("myblobcat5","cat.jpg"))