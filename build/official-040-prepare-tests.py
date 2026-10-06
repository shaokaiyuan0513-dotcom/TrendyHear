from pathlib import Path
app=Path('<工程目录>')
w=Path('<用户目录>/Documents/Codex/2026-10-05/new-chat/work/trendyhear-official')
s=(app/'bundle/main.splash').read_text()
(w/'syntax.splash').write_text('fn check_syntax(){\n'+s+'\n}\n(1)')
card=(w/'confirm-card.splash').read_text()
(w/'card-syntax.splash').write_text('fn check_syntax(){\nlet proposal={}\n'+card+'\n}\n(1)')
prev=Path('<用户目录>/Documents/Codex/2026-10-05/new-chat/work/trendyhear040/workflow-tests.splash').read_text()
pre=prev.split('let DATA=')[0]
pre+='\nlet random_counter=0\nfn random_u32(){random_counter=random_counter+1 return random_counter}\n'
tests=prev[prev.index('fake_now=today()*86400'):].rstrip().removesuffix('(1)')
def replace_fn(s,name,body):
 start=s.index('fn '+name+'('); b=s.index('{',start); level=1;i=b+1; string=False;escape=False
 while level:
  c=s[i]
  if string:
   if escape:escape=False
   elif c=='\\':escape=True
   elif c=='"':string=False
  elif c=='"':string=True
  elif c=='{':level+=1
  elif c=='}':level-=1
  i+=1
 return s[:b+1]+body+s[i-1:]
core=s.split('// UI_BEGIN')[0]
for name,body in [('show',''),('request_source','sent_sources.push(src.url)'),('publish_notice','published=published+1')]:core=replace_fn(core,name,body)
text='偏好清单\n任务：长期订阅\n主题（按优先级）：人工智能｜财经\n用途：了解行业变化\n每日时间：08:30\n每日运行：开启\n我的理解：先关注人工智能，其次财经。\n请在确认卡片中核对并点击确认保存。'
import json
extra='''
let list_text=LIST_TEXT
let parsed=proposal_from_text(list_text)
assert(parsed!=nil && parsed.preferences.topics[0]=="人工智能" && parsed.action=="subscribe")
assert(proposal_from_text("任务：长期订阅") == nil)
assert(proposal_from_text(list_text.replace("人工智能｜财经","人工智能｜财经｜文化｜社会")) == nil)
let before_prefs=state.prefs.to_json()
let before_sequence=state.last_sequence
let before_fetch=sent_sources.len()
bridge_prompt="this connection only"
// Old history and system lane replies cannot create a proposal.
consider_history({messages:[{lane:"person",role:"assistant",content:list_text}]})
assert(pending_proposal==nil)
consider_history({messages:[{lane:"person",role:"user",content:"bootstrap",display_text:bridge_prompt},{lane:"system_agent",role:"assistant",content:list_text}]})
assert(pending_proposal==nil)
// A current assistant proposal creates a card, never saves preferences or starts network.
consider_history({messages:[{lane:"person",role:"user",content:"bootstrap",display_text:bridge_prompt},{lane:"person",role:"assistant",content:list_text}]})
assert(pending_proposal!=nil)
assert(state.prefs.to_json()==before_prefs && state.last_sequence==before_sequence && sent_sources.len()==before_fetch)
assert(host_calls[host_calls.len()-1].service=="glance.publish")
let first_id=pending_proposal.id
consume_confirmation()
assert(state.last_sequence==before_sequence)
// Cancellation leaves all saved preferences unchanged.
decide_proposal("cancel")
assert(pending_proposal==nil && state.prefs.to_json()==before_prefs)
// Stale receipts cannot confirm a replacement proposal.
stage_proposal(parsed)
assert(pending_proposal.id!=first_id)
consume_confirmation()
assert(state.last_sequence==before_sequence)
// Execute the card's real click handler (UI status is a test stub).
let proposal={id:pending_proposal.id}
let ui={result:{set_text:fn(text){return nil}}}
CARD_HANDLER
assert(!submitted)
decide("confirm")
assert(submitted && state.prefs.to_json()==before_prefs)
consume_confirmation()
assert(state.prefs.topics[0]=="人工智能" && state.last_sequence==before_sequence+1 && sent_sources.len()==before_fetch+4)
assert(pending_proposal==nil)
stop()
consume_confirmation()
assert(state.last_sequence==before_sequence+1)
// Expired card refuses the click, and invalidation removes it from app state.
stage_proposal(parsed)
proposal={id:pending_proposal.id} submitted=false
fake_now=fake_now+601
let previous_receipt=files[DATA+"confirmed-action.json"]
decide("confirm")
assert(!submitted && files[DATA+"confirmed-action.json"]==previous_receipt)
consume_confirmation()
assert(pending_proposal==nil)
// User correction invalidates a displayed card before creating any replacement.
stage_proposal(parsed)
consider_history({messages:[{lane:"person",role:"user",content:"bootstrap",display_text:bridge_prompt},{lane:"person",role:"assistant",content:list_text},{lane:"person",role:"user",content:"改成文化优先"}]})
assert(pending_proposal==nil)
// A query card saves a one-time task only.
let temp=proposal_from_text(list_text.replace("任务：长期订阅","任务：单次查询").replace("人工智能｜财经","文化"))
before_prefs=state.prefs.to_json()
stage_proposal(temp) decide_proposal("confirm")
assert(state.prefs.to_json()==before_prefs && state.run_prefs.topics[0]=="文化")
(1)
'''
extra=extra.replace('LIST_TEXT',json.dumps(text,ensure_ascii=False)).replace('CARD_HANDLER',card.split('SolidView{')[0])
(w/'workflow-tests.splash').write_text(pre+core+tests+extra)
