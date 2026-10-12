import re,sys
p=sys.argv[1]+'/src/click/core.py';s=open(p).read()
s=s.replace("    def get_parameter_source(self, name: str)","    def get_parameter_source_name(self, name: str) -> str | None:\n        src = self.get_parameter_source(name)\n        return None if src is None else src.name.lower()\n\n    def get_parameter_source(self, name: str)",1)
s=s.replace("    def parse_args(self, ctx: Context, args: list[str]) -> list[str]:","    def params_by_priority(self, ctx: Context) -> list[str]:\n        return [p.name for p in iter_params_for_processing([], self.get_params(ctx))]\n\n    def parse_args(self, ctx: Context, args: list[str]) -> list[str]:",1)
s=s.replace("class Parameter(ABC):","class Parameter(ABC):\n    is_positional = False\n",1)
s=re.sub(r"(class Argument\((?:Parameter|PositionalParameter)\):)",r"\1\n    is_positional = True\n",s,1)
open(p,'w').write(s)
