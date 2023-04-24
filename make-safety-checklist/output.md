# Recommended Lineworker Safety Checklist

1. Scan the barcode to open this safety checklist on your phone.
2. Review and submit the checklist.

{qr}

{topics}

{name}

{ BUTTON_PANEL }

<script>
document.querySelector('._continue').onclick = async () => {
  const uri = '{ ROOT_URI }/a/log-lineworker-safety-briefing';
  const d = await post(uri + '.json', getDataById());
  redirect(uri, d);
};
</script>
