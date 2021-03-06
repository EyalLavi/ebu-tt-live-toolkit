import logging
from .common import create_loggers
from ebu_tt_live import bindings
from ebu_tt_live.bindings import _ebuttm as metadata
from pyxb import BIND
from pyxb.utils.domutils import BindingDOMSupport

log = logging.getLogger('ebu_dummy_encoder')


def main():
    create_loggers()
    log.info('Dummy XML Encoder')

    tt = bindings.tt(
        sequenceIdentifier='testSequence001',
        sequenceNumber='1',
        timeBase='smpte',
        lang='en-GB',
        head=bindings.head_type(
            metadata.headMetadata_type(
                metadata.documentMetadata()
            ),
            bindings.styling(
                bindings.style(
                    id='ID001'
                )
            ),
            bindings.layout()
        ),
        body=BIND(
            bindings.div_type(
                bindings.p_type(
                    bindings.span_type(
                        'Some example text...'
                    ),
                    bindings.br_type(),
                    bindings.span_type(
                        'And another line'
                    ),
                    id='ID005',
                    begin='00:00:00:50',
                    end='00:00:03:24',
                )
            )
        )
    )

    print(
        tt.toDOM(
            bds=BindingDOMSupport(default_namespace=bindings.Namespace)
        ).toprettyxml(
            indent='  '
        )
    )
    log.info('XML output printed')
