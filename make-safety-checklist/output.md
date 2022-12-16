# Recommended Lineworker Safety Checklist

{qr}

Based on the work you described, here is the recommended safety checklist. Mark the checkboxes and click Run to submit.

{topics}

{name}

<button id="_run" type="button">Run</button>

<script>
document.getElementById('_run').onclick = async () => {
  const uri = '{ ROOT_URI }/a/log-lineworker-safety-briefing';
  const d = await post(uri + '.json', getDataById());
  redirect(uri, d);
};
</script>
