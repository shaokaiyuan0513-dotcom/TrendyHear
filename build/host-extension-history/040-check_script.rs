use makepad_script::*;
fn main() {
 let host=Box::leak(Box::new(ScriptVmHost::new((),())));
 let mut vm=ScriptVm{host,bx:Box::new(ScriptVmBase::new())};
 vm.bx.captured_errors=Some(Vec::new());
 let path=std::env::args().nth(1).expect("script path");
 let code=std::fs::read_to_string(&path).unwrap();
 let result=vm.with_instruction_limit(4_000_000, |vm| vm.eval(ScriptMod{file:path,code:format!("{code}\n;"),..Default::default()}));
 let errors=vm.take_errors();
 for error in &errors {eprintln!("{error}");}
 if !errors.is_empty() {std::process::exit(1);}
 println!("RESULT {result:?}");
}
