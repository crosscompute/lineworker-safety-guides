# Recommended Lineworker Safety Topics

Based on the work you described, here is the list of recommended topics to discuss at your safety briefing.

{topics}

<button id="_run" type="button">Run</button>

<script>
document.getElementById('_run').onclick = async () => {
  const uri = '{ ROOT_URI }/a/log-lineworker-safety-briefing';
  const d = await post(uri + '.json', getDataById());
  redirect(uri, d);
};
</script>
