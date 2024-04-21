import discordrpc

rpc = discordrpc.RPC(app_id=1231554148936192110)

# Upload your image(s) here:
# https://discord.com/developers/applications/<APP ID>/rich-presence/assets

rpc.set_activity(
      state="pip install discord-rpc",
      details="Discord-RPC by Senophyx",
      large_image="pak1umb2gnl34hpj1q7jufa4mo-1e2058efe33070711df92d0987c3092a", # Make sure you are using the same name that you used when uploading the image
      large_text="EterNomm",
      small_image="screenshot_20240420160137", # Make sure you are using the same name that you used when uploading the image
      small_text="Github"
    )



rpc.run()
