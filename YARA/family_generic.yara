rule MAL_Graverobber_Family_Python_Generic
{
    meta:
        family      = "Graverobber"
        description = "Generic rule matching Graverobber variants"
        author      = "rf-peixoto"
        reference   = "github.com/rf-peixoto/Graverobber"
        confidence  = "medium"

    strings:
        $f_aes      = "from AesEverywhere import aes256" ascii
        $f_blox     = "from bloxplorer import bitcoin_explorer" ascii
        $f_form1    = "http://{0}.com/file_form.php" ascii
        $f_fileup   = "fileToUpload" ascii
        $f_node_sig = "Node Signature: {0}" ascii
        $f_qv       = "qv1m3r4" ascii
        $f_lethe    = "River Lethe" ascii
        $f_count    = "CountZero.README.txt" ascii

    condition:
        // Require strong infra (bloxplorer + file_form + fileToUpload)
        // plus at least ONE variant-specific artefact
        $f_blox and $f_form1 and $f_fileup
        and 1 of ($f_node_sig, $f_qv, $f_lethe, $f_count)
}
