rule MAL_Graverobber_Locksmith_Python
{
    meta:
        family      = "Graverobber"
        variant     = "locksmith.py"
        description = "Detects Graverobber locksmith tool"
        author      = "rf-peixoto"
        reference   = "github.com/rf-peixoto/Graverobber"
        confidence  = "high"

    strings:
        $s_even   = "some_secret_even_seed" ascii
        $s_odd    = "some_secret_odd_seed" ascii
        $s_usage1 = "[*] Usage: " ascii
        $s_usage2 = " [node_id] [node_sig]" ascii
        $s_blake  = "blake2s(str(node_id + " ascii

    condition:
        all of ($s_even, $s_odd, $s_blake)
        and all of ($s_usage1, $s_usage2)
}
